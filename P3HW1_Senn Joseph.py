#Joseph Robert Eli Senn
#P3HW1
#10/19/2024
# This program takes a number grade , determines average and displays letter grade for average.



# Collect grades for each module
mod_1 = input('Enter grade for Module 1: ')
mod_2 = input('Enter grade for Module 2: ')
mod_3 = input('Enter grade for Module 3: ')
mod_4 = input('Enter grade for Module 4: ')
mod_5 = input('Enter grade for Module 5: ')
mod_6 = input('Enter grade for Module 6: ')

# Convert grades to float and add to a list
grades = [float(mod_1), float(mod_2), float(mod_3), float(mod_4), float(mod_5), float(mod_6)]

# Determine lowest, highest, sum, and average for grades
low = min(grades)
high = max(grades)
total_sum = sum(grades)
avg = total_sum / len(grades)

# Output results
print ('------------Results------------')
print(f"Lowest grade: {low}")
print(f"Highest grade: {high}")
print(f"Sum of grades: {total_sum}")
print(f"Average grade: {avg:.2f}")

print('-----------------------------------------')

# Determine letter grade for average
if avg >= 90:
    print('Your grade is: A')
elif avg >= 80:
    print('Your grade is: B')
elif avg >= 70:
    print('Your grade is: C')
elif avg >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F')





