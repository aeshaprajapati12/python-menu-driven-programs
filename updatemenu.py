string = input("Enter initial string: ")

while True:

    print("\nUPDATE MENU")
    print("1. Replace first occurrence of a character")
    print("2. Replace last occurrence of a character")
    print("3. Replace all occurrences of a character")
    print("4. Replace character at given position")
    print("5. Replace given character at even index positions")
    print("6. Replace given character at odd index positions")
    print("7. Replace characters between two positions")
    print("8. Replace characters everywhere except first and last")
    print("9. Display current string")
    print("10. Exit")

    choice = int(input("Enter your choice: "))

    # 1. Replace first occurrence
    if choice == 1:
        old = input("Enter character to replace: ")
        new = input("Enter new character: ")

        new_string = ""
        replaced = False
        i = 0

        while i < len(string):
            if string[i] == old and not replaced:
                new_string += new
                replaced = True
            else:
                new_string += string[i]
            i += 1

        string = new_string
        print("Updated String:", string)

    # 2. Replace last occurrence
    elif choice == 2:
        old = input("Enter character to replace: ")
        new = input("Enter new character: ")

        last_index = -1
        i = 0

        while i < len(string):
            if string[i] == old:
                last_index = i
            i += 1

        new_string = ""
        i = 0
        while i < len(string):
            if i == last_index:
                new_string += new
            else:
                new_string += string[i]
            i += 1

        string = new_string
        print("Updated String:", string)

    # 3. Replace all occurrences
    elif choice == 3:
        old = input("Enter character to replace: ")
        new = input("Enter new character: ")

        new_string = ""
        i = 0

        while i < len(string):
            if string[i] == old:
                new_string += new
            else:
                new_string += string[i]
            i += 1

        string = new_string
        print("Updated String:", string)

    # 4. Replace at given position
    elif choice == 4:
        pos = int(input("Enter position (0-based index): "))
        new = input("Enter new character: ")

        new_string = ""
        i = 0

        while i < len(string):
            if i == pos:
                new_string += new
            else:
                new_string += string[i]
            i += 1

        string = new_string
        print("Updated String:", string)

    # 5. Replace at even index positions
    elif choice == 5:
        old = input("Enter character to replace: ")
        new = input("Enter new character: ")

        new_string = ""
        i = 0

        while i < len(string):
            if i % 2 == 0 and string[i] == old:
                new_string += new
            else:
                new_string += string[i]
            i += 1

        string = new_string
        print("Updated String:", string)

    # 6. Replace at odd index positions
    elif choice == 6:
        old = input("Enter character to replace: ")
        new = input("Enter new character: ")

        new_string = ""
        i = 0

        while i < len(string):
            if i % 2 != 0 and string[i] == old:
                new_string += new
            else:
                new_string += string[i]
            i += 1

        string = new_string
        print("Updated String:", string)

    # 7. Replace between two positions
    elif choice == 7:
        start = int(input("Enter start position: "))
        end = int(input("Enter end position: "))
        new = input("Enter replacement character: ")

        new_string = ""
        i = 0

        while i < len(string):
            if i >= start and i <= end:
                new_string += new
            else:
                new_string += string[i]
            i += 1

        string = new_string
        print("Updated String:", string)

    # 8. Replace everywhere except first and last
    elif choice == 8:
        new = input("Enter replacement character: ")

        new_string = ""
        i = 0

        while i < len(string):
            if i == 0 or i == len(string) - 1:
                new_string += string[i]
            else:
                new_string += new
            i += 1

        string = new_string
        print("Updated String:", string)

    # 9. Display string
    elif choice == 9:
        print("Current String:", string)

    # 10. Exit
    elif choice == 10:
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")