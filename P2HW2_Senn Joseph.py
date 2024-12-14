#Joseph Robert Eli Senn
#10/13/2024
#P2HW2
#This code asks the user for the grades to be entered module 1-6 and then displays the lowest grade, highes grade, the sum, and an average of all grades Start the program.

#Pseudocode
# Start the program.
# Initialize an empty list named 'spooky_grades' to store the grades.
# Prompt the user to enter grades for the following modules:
  # a. Module 1
  # b. Module 2
  # c. Module 3
  # d. Module 4
  # e. Module 5
  # f. Module 6
# Convert each input to a float and append it to 'spooky_grades'.
# Calculate the lowest grade using the min() function on 'spooky_grades'.
# Calculate the highest grade using the max() function on 'spooky_grades'.
# Calculate the total sum of grades using the sum() function on 'spooky_grades'.
# Calculate the average grade by dividing the total sum by the number of grades in 'spooky_grades'.
# Display the results:
  # a. Print the lowest grade formatted to two decimal places.
  # b. Print the highest grade formatted to two decimal places.
  # c. Print the total sum of grades formatted to two decimal places.
  # d. Print the average grade formatted to two decimal places.
# End the program.


# Input section
module_1 = float(input("Enter grade for Module 1: "))
module_2 = float(input("Enter grade for Module 2: "))
module_3 = float(input("Enter grade for Module 3: "))
module_4 = float(input("Enter grade for Module 4: "))
module_5 = float(input("Enter grade for Module 5: "))
module_6 = float(input("Enter grade for Module 6: "))

# Creating the list of grades
spooky_grades = [module_1, module_2, module_3, module_4, module_5, module_6]

# Calculate grades for modules
total_sum = sum(spooky_grades)
average_grade = total_sum / 6

# Find lowest and highest grades
lowest_grade = min(spooky_grades)
highest_grade = max(spooky_grades)


# Display section
print("------------Results------------")
print(f"{'Lowest Grade:':<20}{lowest_grade:.1f}")
print(f"{'Highest Grade:':<20}{highest_grade:.1f}")
print(f"{'Sum of Grades:':<20}{total_sum:.1f}")
print(f"{'Average:':<20}{average_grade:.2f}")

print("----------------------------------------")












