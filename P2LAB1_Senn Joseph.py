#Joseph Robert Eli Senn
#10/5/2024
#P2LAB1
#This program asks for the radius of a circle and then displays the Diameter, circumference, and area said circle based off of the input given by the user i.e. the radius.
import math 


#Get radius from user
radius= float(input("What is the radius of the circle? " ))


#Calculate diameter, circumference, and area.
diameter= 2 * radius
circumference= 2 * math.pi * radius
area= math.pi *(radius*radius)

#display results
print(f"The diameter of the circle is {diameter:.1f}")
print(f"The circumference of the circle is {circumference:.2f}")
print(f"The area of the cirle is {area:.3f}")



