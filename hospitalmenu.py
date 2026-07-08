'''
Write a menu-driven program to manage hospital billing with the following options:
1.	Register patient (name and age).
2.	Add doctor consultation fee.
3.	Add medicine charges.
4.	Display final bill.
5.	Exit.
'''

patient_name = ""
patient_age = 0
consultation_fee = 0
medicine_charges = 0

while True:
    print("\n---- Hospital Billing Menu ----")
    print("1. Register Patient")
    print("2. Add Doctor Consultation Fee")
    print("3. Add Medicine Charges")
    print("4. Display Final Bill")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        patient_name = input("Enter patient name: ")
        patient_age = int(input("Enter patient age: "))
        print("Patient registered successfully.")

    elif choice == 2:
        fee = float(input("Enter consultation fee: "))
        consultation_fee += fee
        print("Consultation fee added.")

    elif choice == 3:
        charges = float(input("Enter medicine charges: "))
        medicine_charges += charges
        print("Medicine charges added.")

    elif choice == 4:
        total_bill = consultation_fee + medicine_charges
        print("\n----- Final Bill -----")
        print("Patient Name:", patient_name)
        print("Patient Age:", patient_age)
        print("Consultation Fee:", consultation_fee)
        print("Medicine Charges:", medicine_charges)
        print("Total Bill:", total_bill)

    elif choice == 5:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")