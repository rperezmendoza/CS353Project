Name: Roberto Perez Mendoza
CPSC353 Introduction to Security
Assignment Description: The purpose of this assignment is to encrypt text messages
entered by the user into a selected image  as well as decrypts the message from the 
image in which the message was encrypted. Note that the image(s) need to be in the same 
directory in which the python file is located in order for it to work. 

Note: In order for this program to work, one needs to have pillow installed. Pillow is the 
python imaging library, which will be used for this project. 

How to use the program: This project was used using python 2.xx and has been tested on 
Mac OS terminal titan as well as linux ubuntu mate on a virtual machine. The following commands
were used to successfully satisfy the requirements of the project:
  * Download the zip "p1CPSC353RobertoPerez" file containing the images and the python file.
  * Extract the zip folder and open your terminal
  * Look for the directory and use the following commands:
      - python steganography.py -e legos.png
	+ Note: -e (encrypt) is a selection for encrypting the message into the image
	+ To decrypt, it should be similar, but this time, you should replace
	  -e (encrypt) for -d (decrypt) e.g. python steganography.py -d legos.png
      - Enter a message you wish to encrypt e.g. "It is time to say bye Toys R US "
	then hit enter
      - A successfull message should be displayed. 
      - An error should be displayed if the image is not compatable. 

Output:
Using .png images
roberto@roberto-VirtualBox:~/Desktop/p1CPSC353RobertoPerez$ python ./steganography.py -e legos.png 
Please enter a text to hide in the image: Time to say bye to ToysRus :(
The text has been encrypted to the image.

roberto@roberto-VirtualBox:~/Desktop/p1CPSC353RobertoPerez$ python ./steganography.py -d legos.png 
Retrieve completed.

Time to say bye to ToysRus :(
roberto@roberto-VirtualBox:~/Desktop/p1CPSC353RobertoPerez$ 

Using .JPG images
roberto@roberto-VirtualBox:~$ cd Desktop/p1CPSC353RobertoPerez/
roberto@roberto-VirtualBox:~/Desktop/p1CPSC353RobertoPerez$ python ./steganography.py -e blizzard.JPG 
Please enter a text to hide in the image: I'm a gamer
The text has been encrypted to the image.

roberto@roberto-VirtualBox:~/Desktop/p1CPSC353RobertoPerez$ python ./steganography.py -d blizzard.JPG 
Retrieve completed.

I'm a gamer
roberto@roberto-VirtualBox:~/Desktop/p1CPSC353RobertoPerez$ 

Note: 4 images are included so that they can be tested. 
