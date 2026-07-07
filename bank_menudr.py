'''
Write a menu-driven program using a while loop to perform the following operations:
1.	Create a new bank account (accept account holder name, account number and initial balance).
2.	Deposit amount into the account.
3.	Withdraw amount from the account.
4.	Display current balance.
5.	Exit.
'''



account_holder = ""
account_number = ""
balance = 0
account_created = False

while True:
    print("\n--- BANK MENU ---")
    print("1. Create New Account")
    print("2. Deposit Amount")
    print("3. Withdraw Amount")
    print("4. Display Balance")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    # 1️⃣ Create Account
    if choice == 1:
        account_holder = input("Enter Account Holder Name: ")
        account_number = input("Enter Account Number: ")
        balance = float(input("Enter Initial Balance: "))
        account_created = True
        print("Account created successfully!")

    # 2️⃣ Deposit
    elif choice == 2:
        if account_created:
            amount = float(input("Enter amount to deposit: "))
            balance += amount
            print("Amount deposited successfully!")
        else:
            print("Please create an account first.")

    # 3️⃣ Withdraw
    elif choice == 3:
        if account_created:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= balance:
                balance -= amount
                print("Amount withdrawn successfully!")
            else:
                print("Insufficient balance!")
        else:
            print("Please create an account first.")

    # 4️⃣ Display Balance
    elif choice == 4:
        if account_created:
            print("Account Holder:", account_holder)
            print("Account Number:", account_number)
            print("Current Balance:", balance)
        else:
            print("Please create an account first.")

    # 5️⃣ Exit
    elif choice == 5:
        print("Thank you for using Bank System!")
        break

    else:
        print("Invalid choice! Please try again.")