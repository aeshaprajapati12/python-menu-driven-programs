'''
Write a menu-driven program to:
1.	Enter consumer name and units consumed.
2.	Calculate electricity bill.
3.	Display bill details.
4.	Exit.
'''

consumer_name = ""
units = 0
bill_amount = 0

while True:
    print("\n---- Electricity Billing Menu ----")
    print("1. Enter Consumer Details")
    print("2. Calculate Electricity Bill")
    print("3. Display Bill Details")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        consumer_name = input("Enter consumer name: ")
        units = int(input("Enter units consumed: "))
        print("Consumer details saved successfully.")

    elif choice == 2:
        if units <= 100:
            bill_amount = units * 5

        elif units <= 200:
            bill_amount = (100 * 5) + (units - 100) * 7

        else:
            bill_amount = (100 * 5) + (100 * 7) + (units - 200) * 10

        print("Electricity bill calculated successfully.")

    elif choice == 3:
        print("\n----- Electricity Bill -----")
        print("Consumer Name:", consumer_name)
        print("Units Consumed:", units)
        print("Total Bill Amount: ₹", bill_amount)

    elif choice == 4:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")