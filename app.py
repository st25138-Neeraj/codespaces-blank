
def loading_inventory():
  print("You selected option 1: loading inventory.")    

def displaying_inventory():
   print("You selected option 2: displaying inventory.")

def shopping():
   print("You selected option 3: shopping.")

def displaying_cart():
   print("You selected option 4: displaying cart.")

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
      loading_inventory()    
    elif menu_option == "2":
      displaying_inventory()
    elif menu_option == "3":
      shopping()
    elif menu_option == "4":
        displaying_cart()
    elif menu_option.lower() == "q":
        print("Goodbye")
        break
    else:
        print("Invalid option, please try again.")
