
# CTI-110

# P3HW2 - Salary

# Morales stefan

# 06/13/2023

# Function to calculate pay
def calculate_pay(name, hours_worked, pay_rate):
    overtime_hours = 0
    overtime_pay = 0
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * pay_rate * 1.5
        hours_worked = 40

    regular_pay = hours_worked * pay_rate
    gross_pay = regular_pay + overtime_pay

    return overtime_hours, overtime_pay, regular_pay, gross_pay

# Main program
def main():
    name = input("Enter the employee's name: ")
    hours_worked = float(input("Enter the number of hours worked: "))
    pay_rate = float(input("Enter the employee's pay rate: "))

    overtime_hours, overtime_pay, regular_pay, gross_pay = calculate_pay(name, hours_worked, pay_rate)

    print("------------------------------------------")
    print("Employee name: \n")
    print("Hours Worked      Pay Rate      OverTime       OverTime Pay      RegHour Pay           Gross Pay")
    print("---------------------------------------------------------------------------------------------------------------")
    print(f"{hours_worked}               {pay_rate}           {overtime_hours}            {overtime_pay:.2f}            ${regular_pay:.2f}             ${gross_pay:.2f}")

# Call the main function
if __name__ == "__main__":
    main()
