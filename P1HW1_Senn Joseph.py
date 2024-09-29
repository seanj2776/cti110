#Joseph Robert Eli Senn
#9/27/2024
#P1HW1
#This program allows the user to enter different numerical values for exponent equations as well as addition and subtraction.
print("-----Calculating Exponenets----")
first = int(input("Enter an integer as the base value: "))

second = int(input("Enter an integer as the exponent: "))

result = first ** second

print(f"{first} raised to the power of {second} is {result}!!")

print("-----Addition and Subtraction----")

third = int(input("Enter a starting integer: "))

fourth = int(input("Enter an integer to add: "))

fifth = int(input("Enter an integer to subtract: "))

result = third + fourth - fifth

print(f"{third} + {fourth} - {fifth} is equal to {result}")
