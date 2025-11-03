while True:
    print("----------------------------------")
    print("enter 1 for loading inventory")
    print("enter 2 for displaying inventory")
    print("enter 3 for shopping")
    print("enter 4 for displaying cart")
    print("enter q or Q to quit")
    print("----------------------------------")

    menu_option = input("Enter an option: ")
    print("You have selected", menu_option)

    if menu_option == "1":
        print("You selected option 1: loading inventory.")
    elif menu_option == "2":
        print("You selected option 2: displaying inventory.")
    elif menu_option == "3":
        print("You selected option 3: shopping.")
    elif menu_option == "4":
        print("You selected option 4: displaying cart.")
    elif menu_option.lower() == "q":
        print("Goodbye")
        break
    else:
        print("Invalid option, please try again.")
