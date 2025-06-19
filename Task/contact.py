import json

def cmd():
    print ("1) Add Contact\n2) View Contact\n3) Search Contact\n4) Update Contact\n5) Delete Contact\n6) Exit\n")

def load_contacts():
    try:
        with open("contact.json","r") as f:
            return json.load(f)
    except FileNotFoundError:  
        return{}


def save_contacts(contacts):
    with open("contact.json","w") as f:
         json.dump(contacts, f,indent=4)
 
    

def add_contacts(contacts):

    name = input("Name:- ")
    if name in contacts:
        print(f"{name} already exist")

    else: 
        try:
            phone_number = input("Phone Number:- ")
            if len(phone_number) != 10 or not phone_number.isdigit():
                raise ValueError("Enter a valid 10 -digit number.")
            
            email = input("Email: ")
            contacts[name] = {"Phone": phone_number, "Email ID": email}
            save_contacts(contacts)
            print("Contact added successfully!")

        except ValueError as e:
          print("Error:",e)

def view_contacts(contacts):
    if not contacts:
        print("No contacts found")
    else:
        for name,info in contacts.items():
            print(f"Name:{name}")     
            print(f"Phone:{info['Phone']}")
            print(f"Email:{info['Email ID']}")

def search_contacts(contacts):
    name = input("Name:- ")
    if name in contacts:
        print(f"Phone:{contacts[name]['Phone']}")
        print(f"Email:{contacts[name]['Email ID']}")
    else:
        print("Contact not found")    

def update_contacts(contacts):
     name = input("Name:- ")
     if name in contacts:

        try:
             phone_number =input("Phone Number:- ")                                                                                           
             if len(phone_number) != 10 or not phone_number.isdigit():
                 raise ValueError("Enter a valid 10 -digit number.")
         
             email = input("Email: ")
             contacts[name] = {"Phone": phone_number, "Email ID": email}
             save_contacts(contacts)
             print("Contact updated successfully!")
        except ValueError as e:
              print("Error:",e)
       
     else:  
         print("Contact not found")


def delete_contacts(contacts):
     name = input("Name:- ")
     if name in contacts:
         del contacts[name]
         save_contacts(contacts)
         print("Contact deleted.")
     else:
         print("Contact not found")    



contacts = load_contacts()
while True:
          cmd()
          choice = input (" Enter your choice (1-6):- ")
          if choice == "1":
                add_contacts(contacts)

          elif choice == "2":
               view_contacts(contacts)   

          elif choice == "3":
                search_contacts(contacts)   

          elif choice == "4":
                update_contacts(contacts)       

          elif choice == "5":
                delete_contacts(contacts) 

          elif choice == "6":
                save_contacts(contacts)
                print (" Contact is Saved")
                break

          else:
                print("Enter a valid option. Thank You!")    


   



             
  

