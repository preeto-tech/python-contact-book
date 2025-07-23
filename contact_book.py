contacts={}

while True:
    print("\nContact Book...\n"
          "1. Create Contact\n"
          "2. View Contact\n"
          "3. Update Contact\n" 
          "4. Delete Contact\n"
          "5. Search Contact\n"
          "6. Exit\n")
    choice=input("Enter your choice: ")

    if choice=="1":
        name=input("Enter your name: ")
        if name in contacts:
            print(f"Contact name {name} already exist.")
        else:
            age=int(input("Enter your age: "))
            email=input("Enter your email address: ")
            mobile_no=input("Enter your mobile number: ")
            contacts[name]={"age": age, "email": email, "mobile number": mobile_no }
            print(f"Contact name {name} has been created successfully.")

    elif choice=="2":
        name=input("Enter contact name to view: ")
        if name in contacts:
            contact=contacts[name]
            #print(f"Name: {name}, age: {age}, email: {email}, mobile number: {mobile_no}")
            print(f"Name: {name}, Age: {contact['age']}, Email: {contact['email']}, Mobile Number: {contact['mobile number']}")

        else:
            print("Contact not found!")
    
    elif choice=="3":
        name=input("Enter name to update Contact: ")
        if name in contacts:
            age=int(input("Enter your updated age: "))
            email=input("Enter your updated email address: ")
            mobile_no=int(input("Enter your updated mobile number: "))
            contacts[name]={"age": age, "email": email, "mobile number": mobile_no }
            print(f"Contact {name} has been updated successfully.")

        else:
            print("Contact not found!")

    elif choice=="4":
        name=input("Enter contact name to delete: ")
        if name in contacts:
            del contacts[name]
            print(f"Contact name: {name} has been deleted successfully.")
        else:
            print("Contact not found!")

    elif choice=="5":
        search_name=input("Enter contact name to search: ")
        found= False
        for name, contact in contacts.items():
            if search_name.lower() in name.lower():
                print(f"Found - Name: {name}, Age: {contact['age']}, Email: {contact['email']}, Mobile Number: {contact['mobile number']}")
                found= True
        if not found:
            print("No contact found with that name")

    elif choice=="6":
        print("Exiting contact!, Good bye..")
        break


    else:
        print("Invalid choice! ")
    

