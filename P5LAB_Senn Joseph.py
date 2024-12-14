#Joseph Robert Eli Senn
#11/16/2024
#P5LAB
#This program simulates a self-checkout, calculating and breaking down change into dollars and coins. It generates a random total, prompts the user for payment, and displays the change owed.





import random

# Function to calculate and display the coins needed for change
def disperse_change(change):
    """
    Calculate and display the amount of dollars, quarters, dimes, nickels, and pennies
    needed to make the change.
    """
    # Convert the change to cents
    total_cents = int(change * 100)
    
    # Calculate the number of each coin type
    dollars = total_cents // 100
    total_cents %= 100

    quarters = total_cents // 25
    total_cents %= 25

    dimes = total_cents // 10
    total_cents %= 10

    nickels = total_cents // 5
    total_cents %= 5

    pennies = total_cents

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
    """
    Simulate a self-checkout machine where the user pays and receives change.
    """
    # Generate a random float as the total amount owed
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe: ${amount_owed:.2f}")

    # Prompt the user for the amount they are paying
    try:
        amount_paid = float(input("How much cash will you put in the self-checkout?"))
        
        # Ensure the payment is sufficient
        if amount_paid < amount_owed:
            print("Insufficient payment. Please pay at least the amount owed.")
        else:
            # Calculate the change owed
            change_owed = round(amount_paid - amount_owed, 2)
            print(f"Change is: ${change_owed:.2f}")
            
            # Call the disperse_change function to calculate and display the coins
            if change_owed > 0:
                disperse_change(change_owed)
            else:
                print("No change needed.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

# Call the main function to start the program
if __name__ == "__main__":
    main()
