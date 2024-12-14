#Joseph Robert Eli Senn
#9/27/2024
#P2HW1
#This program asks for a budget amount and then for expenses related to travel destination, finally calculates the difference between the budget and expenses showing the remaining balance.

#Step 1
#print This program calculates and displays travel expenses
#print Enter Budget:
#input budget amount

#Step 2
#print Enter your travel destination:
#input destination

#Step 3
#print How much do you think you will spend on gas?
#input gas amount

#Step 4
#print Approximately, how much will you need for accomodation/hotel?
#input hotel amount'

#Step 5
#print Last, how much do you need for food?
#input food amount

#Step 6
#print ------------Travel Expenses------------

#Step 7
#print location
#print location input

#Step 8
#print Initial Budget:
#print budget input

#Step 9
#print Fuel:
#print fuel input

#Step 10
#print Accomodation:
#print accomodation input

#Step 11
#print Food
#print food input

#Step 12
#calculate total amount of expenses= gas+accomodation+food
#subtract total expenses from budget=remaining balance

#Step 13
#print balance_balance

# Your Name
# Date: YYYY-MM-DD
# Assignment Name: P2HW1
# A brief description of the project: This program calculates and displays travel expenses.

# Input section
print("This program calculates and displays travel expenses")
budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas = float(input("How much do you think you will spend on gas? "))
accommodation = float(input("Approximately, how much will you need for accommodation/hotel? "))
food = float(input("Last, how much do you need for food? "))

# Display section
print("\n------------ Travel Expenses ------------")
print(f"{'Location:':<20} {destination}")
print(f"{'Initial Budget:':<20} ${budget:,.2f}")
print(f"{'Fuel:':<20} ${gas:,.2f}")
print(f"{'Accommodation:':<20} ${accommodation:,.2f}")
print(f"{'Food:':<20} ${food:,.2f}")
print("-----------------------------------------")



# Calculate remaining balance
total_expenses = gas + accommodation + food
remaining_balance = budget - total_expenses

print(f"{'Remaining Balance:':<20} ${remaining_balance:,.2f}")



