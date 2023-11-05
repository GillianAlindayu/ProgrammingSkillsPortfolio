# Getting started with python 

# Exercise 1: strings 

print("twinkle, twinkle little star, \n\t how I wonder what you are! \n\t\t Up above the world so high!,  \n\t\t  like a diamond in the sky, \n\t\t Twinke Twinkle little star, How I wonder what you are! ")

# Exercise 2: Write a program to print the version of python version that you are using: ballot_box_with_check: 
#this is the solution of exercise: 

#python version 

import sys 
print("python version")
print(sys.version)
print("version info. ")
print(sys.version_info)

# Exercise 3: print date and time: ballot_box_with_check: 
#write a python program to display the current date and time: 

from datetime import date 

today = date.today()

#dd/mm/yy
d1 = today.strftime("%d/ %m /%y")
print("d1 =", d1)

#Textual month, date, and year
d2 = today.strftime("%b %b, %y")
print("d2 =", d2)

#mm/dd/yy
d3 = today.strftime("%m/%d/%y")
print("d3 =", d3)

# month abbreviation day, and year 
d4 = today.strftime("%b-%d-%y")
print("d4 =", d4)

# Evercise 4: strings concatination: ballot_box_with_check: 
#Write three strings in different variables and print output of one

# This program is creating variable 

a = "hello"
b = "there,"
c = "mate"

print( a, "" + b, "" + c )

# Exercise 5: compute the area of the circle: ballot_box_with_check: 
#Write a python program which accepts the radius of the circle from the user and compute the area. 

#Here's the solution of finding the area of the circle:
import math as M
Radius = float(input("please enter the radius of the given cicle:"))
area_of_the_circle = M.pi* Radius*Radius 
print(" The area of the given circle is:", area_of_the_circle)


