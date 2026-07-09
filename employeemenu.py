'''

Write a menu-driven program that performs:
1.	Enter employee name and basic salary.
2.	Calculate salary components.
3.	Display salary slips.
4.	Exit.
'''


employee_name = ""
basic_salary = 0

hra = da = pf = 0
gross_salary = 0
net_salary = 0

while True:
    print("\n---- Employee Salary Menu ----")
    print("1. Enter Employee Details")
    print("2. Calculate Salary Components")
    print("3. Display Salary Slip")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        employee_name = input("Enter employee name: ")
        basic_salary = float(input("Enter basic salary: "))
        print("Employee details saved successfully.")

    elif choice == 2:
        hra = basic_salary * 0.20
        da = basic_salary * 0.10
        pf = basic_salary * 0.05

        gross_salary = basic_salary + hra + da
        net_salary = gross_salary - pf

        print("Salary calculated successfully.")

    elif choice == 3:
        print("\n----- Salary Slip -----")
        print("Employee Name:", employee_name)
        print("Basic Salary:", basic_salary)
        print("HRA (20%):", hra)
        print("DA (10%):", da)
        print("PF (5%):", pf)
        print("Gross Salary:", gross_salary)
        print("Net Salary:", net_salary)

    elif choice == 4:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")