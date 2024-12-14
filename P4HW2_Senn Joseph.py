# Joseph Robert Eli Senn    
# 11/10/2024
# P4HW2
# A brief description: This program calculates the pay for multiple employees,  including overtime and regular pay, and computes total amounts for each category.


# 1. Initialize variables for total overtime, total regular pay, total gross pay, and employee count.
# 2. Prompt the user for the employee's name.
# 3. If the name is "Done", break out of the loop.
# 4. Otherwise, ask for the employee's hourly pay rate and hours worked.
# 5. Calculate regular pay and overtime pay based on hours worked.
# 6. Update the total overtime, total regular pay, total gross pay, and employee count.
# 7. Display employee's hours worked, pay rate, overtime pay, regular pay, and gross pay after each entry.
# 8. Repeat until the user enters "Done".
# 9. Output the total overtime, regular pay, gross pay, and the number of employees processed.





def main():
    # Step 1: Initialize totals and employee count
    total_overtime = 0
    total_regular = 0
    total_gross = 0
    employee_count = 0

    # Step 2: Ask for the first employee's details
    while True:
        # Ask for employee name
        employee_name = input("Enter employee's name or 'Done' to terminate: ")
        
        # If user enters "Done", exit the loop
        if employee_name.lower() == "done":
            break
        
        # Step 3: Get pay rate and hours worked
        try:
            hours_worked = float(input(f"How many hours did {employee_name} work? "))
            pay_rate = float(input(f"What is {employee_name}'s pay rate? "))
        except ValueError:
            print("Invalid input. Please enter valid numbers for pay rate and hours worked.")
            continue
        
        # Step 4: Calculate regular and overtime pay
        if hours_worked > 40:
            regular_pay = 40 * pay_rate  # Regular pay is for first 40 hours
            overtime_hours = hours_worked - 40  # Overtime hours
            overtime_pay = overtime_hours * (pay_rate * 1.5)  # Overtime pay is 1.5 times the hourly rate
        else:
            regular_pay = hours_worked * pay_rate  # No overtime
            overtime_hours = 0
            overtime_pay = 0
        
        # Step 5: Calculate gross pay
        gross_pay = regular_pay + overtime_pay
        
        # Step 6: Update totals
        total_overtime += overtime_pay
        total_regular += regular_pay
        total_gross += gross_pay
        employee_count += 1
        
        # Step 7: Display employee name and headers for each employee
        print(f"\nEmployee name:  {employee_name}\n")
        print(f"{'Hours Worked':<15}{'Pay Rate':<10}{'OverTime':<10}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<15}")
        print("-" * 70)
        
        # Step 8: Display employee details with aligned columns and dollar signs
        print(f"{hours_worked:<15.2f}{pay_rate:<10.2f}{overtime_hours:<10.2f}"
              f"${overtime_pay:>12,.2f}     ${regular_pay:>10,.2f}     ${gross_pay:>10,.2f}")
    
    # Step 9: Display results after the loop ends
    print("-" * 70)  # Separator for results
    print(f"Total number of employees entered: {employee_count}")
    print(f"Total amount paid for overtime:   ${total_overtime:>10,.2f}")
    print(f"Total amount paid for regular hours: ${total_regular:>10,.2f}")
    print(f"Total amount paid in gross:       ${total_gross:>10,.2f}")

# Call the main function to run the program
if __name__ == "__main__":
    main()
