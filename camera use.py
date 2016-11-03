import picamera
import time
import os

def photo(cam):
    #Flips the image horizontally then reverts
    name = str(input("\nName of image: "))
    cam.capture(name+'.jpg')

def hflipC(cam):
    #Flips the image horizontally then reverts
    name = str(input("\nName of image: "))
    cam.hflip = True
    cam.capture(name+'.jpg')
    cam.hflip = False

def vflipC(cam):
    #Flips the image vertically then reverts
    name = str(input("\nName of image: "))
    cam.vflip = True
    cam.capture(name+'.jpg')
    cam.vflip = False

def hvflipC(cam):
    #Flips the image horizontally and vertically then reverts
    name = str(input("Name of image: "))
    cam.vflip = True
    cam.hflip = True
    cam.capture(name+'.jpg')
    cam.vflip = False
    cam.hflip = False

def sequence(cam):
    #Creates a sequence of images
    x = 0
    num = 1
    nums = str(num)
    name = str(input("Name of images: "))
    valid = False
    while not valid:
        try:
            amount = int(input("Amount of pictures to be taken(2 - 20): "))
            inter = int(input("Interval between pictures in seconds(1 or above): "))
            if 2 <= amount <= 20 and 1 <= inter:
                valid = True
            else:
                print("\nA value is not valid. Please enter your values again.\n")
        except ValueError:
            print("\nA value is not valid. Please enter your values again.\n")

    while x < amount:
        cam.capture(name+nums+'.jpg')
        time.sleep(inter)
        x = x + 1
        num = num + 1
        nums = str(num)

def gifmaker(cam):
    #Makes a gif from 10 images
    name = str(input("\nName of gif: "))
    valid = False
    while not valid:
        try:
            inter = int(input("Interval between pictures in seconds(1 or above): "))
            if 1 <= inter:
                valid = True
            else:
                print("\nValue is not valid. Please enter your value again.\n")
        except ValueError:
            print("\nValue is not valid. Please enter your value again.\n")
            
    for i in range(10):
        cam.capture('image{0:04d}.jpg'.format(i))

    os.system('convert -delay 10 -loop 0 image*.jpg'+name+'.gif')

def display():
    #Displays the menu
    print("This is a picture capturing program")
    print("Options:")
    print("1. Take a picture\n2. Take a horizontally flipped picture\n3. Take a vertically flipped picture\n4. Take a vertically and horizontally flipped picture\n5.Take a sequence of pictures with an interval inbetween\n6. Make a GIF from 10 pictures\n7. Exit")

def menuChoice():
    option = False
    while not option:
        try:
            choice = int(input("Option Selected: "))
            if 0 <= choice <= 7:
                option = True
            else:
                print("Option not valid. Please enter your option again.")
        except ValueError:
            print("Option not valid. Please enter your option again.")
    return choice

def main():
    #The main program
    camera = picamera.PiCamera()
    noexit = True
    while noexit:
        display()
        option = menuChoice()
        if option == 1:
            photo(camera)
        elif option == 2:
            hflipC(camera)
        elif option == 3:
            vflipC(camera)
        elif option == 4:
            hvflipC(camera)
        elif option == 5:
            sequence(camera)
        elif option == 6:
            gifmaker(camera)
        else:
            noexit = False
            print("Thank you for using my program. Goodbye.")

main()
            
