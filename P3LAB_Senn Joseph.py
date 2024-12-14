#Joseph Robert Eli Senn
#P3LAB
#10/19/2024
#This program calculates the number of dollars, quarters, dimes, nickels, and pennies



def calculate_coins(amount):
    # Convert amount to cents
    total_cents = int(amount * 100)
    
    # Calculate number of each coin type
    dollars = total_cents // 100
    total_cents %= 100
    
    quarters = total_cents // 25
    total_cents %= 25
    
    dimes = total_cents // 10
    total_cents %= 10
    
    nickels = total_cents // 5
    total_cents %= 5
    
    pennies = total_cents // 1

    # Output the results
    if dollars > 0:
        print(f"{dollars} dollar{'s' if dollars > 1 else ''}")
    if quarters > 0:
        print(f"{quarters} quarter{'s' if quarters > 1 else ''}")
    if dimes > 0:
        print(f"{dimes} dime{'s' if dimes > 1 else ''}")
    if nickels > 0:
        print(f"{nickels} nickel{'s' if nickels > 1 else ''}")
    if pennies > 0:
        print(f"{pennies} penn{'ies' if pennies > 1 else 'y'}")

def main():
    # User input
    try:
        amount = float(input("Enter the amount of money as a float: "))
        
        if amount == 0:
            print("No change")
        else:
            calculate_coins(amount)
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()
