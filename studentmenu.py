'''
Write a menu-driven program to perform the following:
1.	Enter student details (name, roll number and marks of three subjects).
2.	Calculate total and percentage.
3.	Display report card.
4.	Exit.
'''

student_name = ""
roll_number = 0
mark1 = mark2 = mark3 = 0
total = 0
percentage = 0

while True:
    print("\n---- Student Report Card Menu ----")
    print("1. Enter Student Details")
    print("2. Calculate Total and Percentage")
    print("3. Display Report Card")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        student_name = input("Enter student name: ")
        roll_number = int(input("Enter roll number: "))
        mark1 = float(input("Enter marks of Subject 1: "))
        mark2 = float(input("Enter marks of Subject 2: "))
        mark3 = float(input("Enter marks of Subject 3: "))
        print("Student details saved successfully.")

    elif choice == 2:
        total = mark1 + mark2 + mark3
        percentage = total / 3
        print("Total and Percentage calculated successfully.")

    elif choice == 3:
        print("\n----- Report Card -----")
        print("Name:", student_name)
        print("Roll Number:", roll_number)
        print("Marks:")
        print("Subject 1:", mark1)
        print("Subject 2:", mark2)
        print("Subject 3:", mark3)
        print("Total Marks:", total)
        print("Percentage:", percentage, "%")

    elif choice == 4:
        print("Exiting program...")
        print("Thanks for visiting our school")
        break

    else:
        print("Invalid choice! Please try again.")