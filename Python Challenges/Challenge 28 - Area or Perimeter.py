#Challenge 28
import os

volumeCheck = input("Is your shape 3D? Y/N: ").upper()
length = int(input("What is the length of your shape? "))
width = int(input("What is the width of your shape? "))
if "Y" in volumeCheck:
    height = int(input("What is the height of your shape? "))
print("")

response = ""

def area():
    shapeArea = length * width
    print("Area = ",shapeArea)

def perimeter():
    shapePerimeter = length*2 + width*2
    print ("Perimeter = ", shapePerimeter)

def volume():
    shapeVolume = length * width * height
    print("Volume = ", shapeVolume)

while "A" not in response and "P" not in response and "V" not in response:
    response = input("Do you want to calculate area, perimeter, or volume? Enter A, P or V (or a combination e.g. 'AV': ").upper()
    print("")
    if "A" in response:
        area()
    if "P" in response:
        perimeter()
    if "V" in response and "Y" in volumeCheck:
        volume()

os.system("pause")
