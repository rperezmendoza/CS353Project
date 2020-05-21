#Programmer: Roberto Perez Mendoza
#CPSC353 
#Project1
#Description: This program was created using python 2.xx as the titan server
#has this version as the current. 

#This is the python image library 
#Note that python pillow must be downloaded for PIL to work
from PIL import Image

import optparse
import binascii

#Convertion from rgb values to hex values function
def rgb2hex(r, g, b):
	#return the value
	return '#{:02x}{:02x}{:02x}'.format(r, g, b)

#Hex to RGB function
def hex2rgb(hexadec):
	return tuple(map(ord, hexadec[1:].decode('hex')))

#string to binary function
def str2bin(text):
	bi = bin(int(binascii.hexlify(text), 16))
	return bi[2:]


#function from binary to string
def bin2str(bi):
	text = binascii.unhexlify('%x' % (int('0b'+bi,2)))
	return text

#Function to encrypt the message into the image
def encode(hexadec, val):
	if hexadec[-1] in ('0','1', '2', '3', '4', '5'):
		hexadec = hexadec[:-1] + val
		return hexadec
	else:
		return None

#function to decrypt the message from image
def decode(hexadec):
	if hexadec[-1] in ('0', '1'):
		return hexadec[-1]
	else:
		return None

#function to hide message and open the image file
def hide(f, text):
	img = Image.open(f)
	bi = str2bin(text) + '1111111111111110'
	#if statement to makesure that the image being used is compatible to RGBA
	if img.mode in ('RGBA'):
		#image is in correct format
		img = img.convert('RGBA')
		#set a variable d for the image data, which returns
		#pixels inside the image
		d = img.getdata()
		
		#new list
		nData = []
		#set value to 0
		val = 0
		temp = ''

		#for-loop for each pixel of the image
		for i in d:
			#if statement to store data if the value if less than the
			#length of the binary
			if (val < len(bi)):
				#encrypt data
				#i[0] for red, i[1] for green, i[2] for blue
				#b[val] is being used for storing
				npixel = encode(rgb2hex(i[0],i[1],i[2]),bi[val])
				if npixel == None:
					#don't make any changes
					nData.append(i)
				else:
					#create a new pixel and save it to the data
					r, g, b = hex2rgb(npixel)
					#set new data to append r,g,b values
					nData.append((r,g,b,255))
					val += 1
			else:
				nData.append(i)

		#Creates and save new data to image	
		img.putdata(nData)
		img.save(f, "PNG")
		return "The text has been encrypted to the image.\n"	
		#return 1
		#Print a completion encryption message
			
	return "Text encryption Error!!\n"

						
#Function to retrieving 
def retr(f):
	img = Image.open(f)
	bi = ''
	
	#for-loop to itirate back to pixels
	if img.mode in ('RGBA'): 
		img = img.convert('RGBA')
		d = img.getdata()
		
		for i in d:
			#this is to grab value from the current pixel
			#i[0] is for red, i[1] is for gree, i[2] is for blue
			val = decode(rgb2hex(i[0],i[1],i[2]))
			#if statement if data is not being found from a 
			#specific pixel
			if val == None:
				#moves tothe next pixel
				pass
			else:
				#when data is found
				bi = bi + val
				#find the delimeter Note: 16 = l delimeter
				#In which 1 delimeter is the last 16 characters
				#of a binary
				if (bi[-16:] == '1111111111111110'):
					#returns binary into string
					print "Retrieve completed.\n"
					return bin2str(bi[:-16])

		return bin2str(bi)
	return "Retrieve Error!!\n"

#main function
def Main():
	parser = optparse.OptionParser('usage %prog '+\
		'-e/-d <target file>')

	#message encryption selection from user's input
	parser.add_option('-e', dest='hide', type='string', \
		help='target picture path to hide text')

	#message decryption selection from user's input
	parser.add_option('-d', dest='retr', type='string', \
		help='target picture path to retrieve text')
	
	(options, args) = parser.parse_args()

	#check for user input text selection to hide it in the image
	if (options.hide != None):
		t = raw_input("Please enter a text to hide in the image: ")
		print hide(options.hide, t)

	#This is to print message being retrieved
	elif (options.retr != None):
		print retr(options.retr)
	else:
		print parser.usage
		exit(0)

if __name__ == '__main__':
	Main()



