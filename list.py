contacts= {}
while True:
    text= "welcome to your contact manager!!!"
    print(text.title().center(52, "*"))
    print("1. Add contacts.".title())
    print("2. view all contacts".title())
    print("3. search contact.".title())
    print("4. delete contact.".title())
    print("5. exit".title())
    choice=input("enter the number of the choice you want: ")
    if choice=="1":
        name=input("ENTER THE NAME OF THE CONTACT: ").strip()
        #.strip() very useful if there is possibility of hidden space
        while name=="":
            print("enter a contact name!!!! ")
            name=input("enter a valid name: ")
        name= name.title()
        contact=input(f"enter {name} number to be added to your contacts: ".upper())
        while contact=="":
            print("enter a contact number!!!!! ")
            contact=input("enter a valid number: ")
       
        contacts[name]= contact
        print(f"{name} contact has been sucsessfully stored.")
    elif choice=="2":
        if not contacts:
            print("no contacts found!!!!!!!".capitalize())
        else:
            for name, contact in contacts.items():
                print(f" {name}: {contact}")
                
    elif choice=="3":
        search=input("enter the name to be searched: ")
        print(f"{search} :{contacts.get(search, "Not Found!!!!")}")
    elif choice=="4":
        delete=input("enter the contact to be deleted: ").strip()
        delete= delete.title()
        if delete in contacts: 
            del contacts[delete]
            print(f" DELETED SUSCESSFULLY!!!")
        else:
            print(f" not found")
    elif choice=="5":
        print("THANKS FOR USING CONTACT MANAGER!!!!!!")
        break
    