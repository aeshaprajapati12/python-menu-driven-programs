'''
Write a menu-driven program that:
1.	Prompts user to login (username and password).
2.	Displays success or failure.
3.	Exit.
'''

correct_username = "admin"
correct_password = "1234"

while True:
    print("\n---- Login Menu ----")
    print("1. Login")
    print("2. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username == correct_username and password == correct_password:
            print("Login Successful ✅")
        else:
            print("Login Failed ❌")

    elif choice == 2:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")