'''
Write a menu-driven program that allows:
1.	Enter customer name.
2.	Add food item cost.
3.	Display total bill.
4.	Exit.
'''

customer_name = ""
total_bill = 0

while True:
    print("\n---- Restaurant Billing Menu ----")
    print("1. Enter Customer Name")
    print("2. Add Food Item Cost")
    print("3. Display Total Bill")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        customer_name = input("Enter customer name: ")
        print("Customer name saved successfully.")

    elif choice == 2:
        cost = float(input("Enter food item cost: "))
        total_bill += cost
        print("Food item added successfully.")

    elif choice == 3:
        print("\n----- Bill Details -----")
        print("Customer Name:", customer_name)
        print("Total Bill Amount: ₹", total_bill)

    elif choice == 4:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")