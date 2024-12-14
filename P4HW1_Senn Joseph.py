
#Joseph Robert Eli Senn
#11/10/2024
#P4HW1
# This program collects user input scores, validates them, removes the lowest score, calculates the average of the remaining scores, and displays the corresponding letter grade.

# Start

# Prompt the user to enter how many scores they wish to input.

# Initialize an empty list to store the valid scores.

# Use a loop to collect the user's scores:

# After collecting all the scores:
 
# Display:
    
# End



def main():
    # Step 1: Ask the user how many scores they want to input.
    num_scores = int(input("How many scores would you like to enter? "))
    
    # Initialize an empty list to hold the scores.
    scores = []
    
    # Step 2: Collect valid scores using a loop.
    for i in range(num_scores):
        while True:
            try:
                score = float(input(f"Enter score #{i + 1}: "))
                
                # Step 3: Validate if the score is between 0 and 100.
                if 0 <= score <= 100:
                    scores.append(score)
                    break
                else:
                    print("INVALID Score entered!!!!")
                    print("Score should be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
    
    # Step 4: Calculate the lowest score and remove it from the list.
    lowest_score = min(scores)
    scores.remove(lowest_score)
    
    # Step 5: Calculate the average of the remaining scores.
    average_score = sum(scores) / len(scores)
    
    # Step 6: Determine the letter grade based on the average score.
    if average_score >= 90:
        letter_grade = 'A'
    elif average_score >= 80:
        letter_grade = 'B'
    elif average_score >= 70:
        letter_grade = 'C'
    elif average_score >= 60:
        letter_grade = 'D'
    else:
        letter_grade = 'F'
    
    # Step 7: Display the results.
    print('--------------Results---------------')
    print(f"\nLowest score entered: {lowest_score}")
    print(f"Modified List: {scores}")
    print(f"Scores Average: {average_score:.2f}")
    print(f"Grade: {letter_grade}")
    print('--------------------------------------')

# Call the main function to run the program
if __name__ == "__main__":
    main()
