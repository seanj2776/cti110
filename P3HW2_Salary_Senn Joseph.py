#Joseph Robert Eli Senn
#P3HW2
#10/26/2024
# This program asks the user for information like hours worked and other info related to their job and calculates a breakdown of their pay info for that time they have entered.


#begin program

#asks for employee name

#asks user for how many hours worked

#ask user for the employee's pay rate

#calculate with the given info to get various info

#show the user the information gotten from previous calculations ie.. employee name, pay rate, hours total worked, overtime pay and regular pay



def calculate_pay():
    # Input employee details
    employee_name = input("Enter employee's name: ")
    hours_worked = float(input("Enter number of hours worked: "))
    pay_rate = float(input("Enter employee's pay rate: "))

    # Initialize variables
    if hours_worked > 40:
        regular_hours = 40
        overtime_hours = hours_worked - regular_hours
    else:
        regular_hours = hours_worked
        overtime_hours = 0

    # Calculate pay
    regular_pay = regular_hours * pay_rate
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    gross_pay = regular_pay + overtime_pay

    # Display results with proper spacing
    print("\nEmployee Name:         ", employee_name)
    print("Pay Rate:                ", format(pay_rate, '.2f'))
    print("Number of Hours Worked:  ", hours_worked)
    print("Overtime Hours:          ", overtime_hours)
    print("Overtime Pay:            ", format(overtime_pay, '.2f'))
    print("Pay for Regular Hours:   $", format(regular_pay, '.2f'))
    print("Gross Pay:               $", format(gross_pay, '.2f'))
   

# Execute the program
calculate_pay()

