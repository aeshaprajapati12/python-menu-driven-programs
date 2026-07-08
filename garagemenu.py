'''
Write a menu-driven program for a garage with the following options:
1.	Enter customer and vehicle details.
2.	Add Oil Change service.
3.	Add Wheel Alignment service.
4.	Add Car Wash service.
5.	Display final bill.
6.	Exit.
'''

customer_name = ""
vehicle_number = ""

oil_change_charge = 0
wheel_alignment_charge = 0
car_wash_charge = 0

# Fixed service charges
OIL_CHANGE_PRICE = 1000
WHEEL_ALIGNMENT_PRICE = 1500
CAR_WASH_PRICE = 500

while True:
    print("\n---- Garage Service Menu ----")
    print("1. Enter Customer and Vehicle Details")
    print("2. Add Oil Change Service")
    print("3. Add Wheel Alignment Service")
    print("4. Add Car Wash Service")
    print("5. Display Final Bill")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        customer_name = input("Enter customer name: ")
        vehicle_number = input("Enter vehicle number: ")
        print("Customer details saved successfully.")

    elif choice == 2:
        oil_change_charge += OIL_CHANGE_PRICE
        print("Oil Change service added.")

    elif choice == 3:
        wheel_alignment_charge += WHEEL_ALIGNMENT_PRICE
        print("Wheel Alignment service added.")

    elif choice == 4:
        car_wash_charge += CAR_WASH_PRICE
        print("Car Wash service added.")

    elif choice == 5:
        total_bill = oil_change_charge + wheel_alignment_charge + car_wash_charge

        print("\n----- Final Bill -----")
        print("Customer Name:", customer_name)
        print("Vehicle Number:", vehicle_number)
        print("Oil Change Charge:", oil_change_charge)
        print("Wheel Alignment Charge:", wheel_alignment_charge)
        print("Car Wash Charge:", car_wash_charge)
        print("Total Bill:", total_bill)

    elif choice == 6:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")