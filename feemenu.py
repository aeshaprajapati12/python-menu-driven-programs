'''
Write a menu-driven program to:
1.	Enter student name and total fee.
2.	Pay fee amount.
3.	Display remaining fee.
4.	Exit.
'''

student_name = ""
total_fee = 0
paid_fee = 0

while True:
    print("\n---- Student Fee Menu ----")
    print("1. Enter Student Details")
    print("2. Pay Fee Amount")
    print("3. Display Remaining Fee")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        student_name = input("Enter student name: ")
        total_fee = float(input("Enter total fee: "))
        paid_fee = 0   # Reset paid fee
        print("Student details saved successfully.")

    elif choice == 2:
        amount = float(input("Enter fee amount to pay: "))
        
        if amount <= (total_fee - paid_fee):
            paid_fee += amount
            print("Payment successful.")
        else:
            print("Amount exceeds remaining fee!")

    elif choice == 3:
        remaining_fee = total_fee - paid_fee
        
        print("\n----- Fee Details -----")
        print("Student Name:", student_name)
        print("Total Fee:", total_fee)
        print("Paid Fee:", paid_fee)
        print("Remaining Fee:", remaining_fee)

    elif choice == 4:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")