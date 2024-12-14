
# Joseph Robert Eli Senn
# 11/22/2024
# P5HW 
#  This program presents a math quiz where the user can choose between addition or subtraction operations, guesses the result, and gets feedback until they choose to exit.

import random

# Function to generate two random numbers
def generate_numbers():
    return random.randint(1, 100), random.randint(1, 100)

# Function to handle addition quiz
def addition_quiz():
    # Generate two random numbers
    num1, num2 = generate_numbers()
    
    # Display the math problem
    print(f"\n  {num1}")
    print(f"+ {num2}")
    
    # Calculate the correct answer
    correct_answer = num1 + num2
    
    # Variable to keep track of the number of guesses
    guesses = 0
    user_answer = None

    # Loop until the user guesses the correct answer
    while user_answer != correct_answer:
        # Get the user's guess
        try:
            user_answer = int(input("Enter answer: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        guesses += 1
        
        # Check if the guess is correct, too high, or too low
        if user_answer == correct_answer:
            print("Congratulations!!!! Your answer is correct.")
            print(f"Number of guesses: {guesses}")
        elif user_answer < correct_answer:
            print("Sorry, guess is too low.")
        else:
            print("Sorry, guess is too high.")

# Function to handle subtraction quiz
def subtraction_quiz():
    # Generate two random numbers
    num1, num2 = generate_numbers()
    
    # Display the math problem
    print(f"\n  {num1}")
    print(f"- {num2}")
    
    # Calculate the correct answer
    correct_answer = num1 - num2
    
    # Variable to keep track of the number of guesses
    guesses = 0
    user_answer = None

    # Loop until the user guesses the correct answer
    while user_answer != correct_answer:
        # Get the user's guess
        try:
            user_answer = int(input("Enter answer: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        guesses += 1
        
        # Check if the guess is correct, too high, or too low
        if user_answer == correct_answer:
            print("Congratulations!!!! Your answer is correct.")
            print(f"Number of guesses: {guesses}")
        elif user_answer < correct_answer:
            print("Sorry, guess is too low.")
        else:
            print("Sorry, guess is too high.")

# Function to display the menu
def display_menu():
    print("\nMAIN MENU")
    print("-" * 20)
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit")

# Main function to drive the program
def main():
    print("Welcome to Math Quiz")
    while True:
        # Display the menu
        display_menu()
        
        # Get user choice
        try:
            choice = int(input("Please choose one of the menu options: "))
        except ValueError:
            print("Invalid choice. Please enter 1, 2, or 3.")
            continue
        
        if choice == 1:
            addition_quiz()
        elif choice == 2:
            subtraction_quiz()
        elif choice == 3:
            print("Thank you for playing...")
            print("Bye!!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Run the main function
if __name__ == "__main__":
    main()
