#Joseph Robert Eli Senn
#11/4/2024
#P4LAB2
#This program asks the user to enter a number and then displays the multiplacation table of said number.

def display_multiplication_table(number):
    print(f"\nMultiplication table for {number}:")
    for i in range(1, 13):  # For loop to create the multiplication table
        print(f"{number} x {i} = {number * i}")

def main():
    while True:  # While loop to allow repeated execution
        try:
            user_input = int(input("Enter an integer: "))
            if user_input >= 0:
                display_multiplication_table(user_input)
            else:
                print("This program does not handle negative number's")
        except ValueError:
            print("Invalid input. Please enter an integer.")

        run_again = input("\nWould you like to run it again? (yes/no): ").strip().lower()
        if run_again != "yes":
            print("Exiting program...")
            break

if __name__ == "__main__":
    main()
