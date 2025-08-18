class Contact:
    def __init__(self):
        self.info = {}
    def set_contact(self,dic):
        self.info = dic
    def get_contact(self):
        return self.info
    
class PhoneBook :
    def __init__(self):
       self.contacts = []
    def add_contact(self,contact):
        self.contacts.append(contact)
        print(f"Contact {contact.get_contact()} was added")
    def display_contacts(self):
        for i in self.contacts :
            print(i.get_contact())
    def search_contact(self,name):
        for contact in self.contacts:
            if name in contact.get_contact().values():
                print(f"Found contact  {contact.get_contact()} .")
    def delete_contact(self,name):
        for contact in self.contacts:
            if name in contact.get_contact().values():
                self.contacts.remove(contact)
                print(f"{contact.get_contact()} was deleted")
    def update_contact(self,cont,name):
        for contact in self.contacts:
            if name in contact.get_contact().values():
                self.contacts.remove(contact)
                self.contacts.append(cont)
                print(f"{contact.get_contact()} was updated to {cont.get_contact()}")
pb= PhoneBook()
contact =Contact()
choice = 0
while choice != 6:
    print("-----------Phone Book ------------")
    print("Press 1 to add Contact")
    print("Press 2 to delete Contact")
    print("Press 3 to display Contacts")
    print("Press 4 to search Contacts")
    print("Press 5 to update Contact")
    print("Press 6 to exit")
    choice = int(input("Enter:"))
    if choice == 1:
        print("***Add Contact***")
        name = input("Enter Name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        contact.set_contact({"Name":name,"Phone":phone,"Email":email})
        pb.add_contact(contact)
    elif choice == 2:
        print("***Delete Contact***")
        name = input("Enter Name of Contact to Delete: ")
        pb.delete_contact(name)
    elif choice == 3:
        print("***Display Contact***")
        pb.display_contacts()
    elif choice == 4:
        print("***Search***")
        name = input("Enter Name to find :")
        pb.search_contact(name)
    elif choice == 5:
        print("***Update Contact***")
        name = input("Enter Name to update: ")
        phone = input("Enter phone to update: ")
        email = input("Enter email to update: ")
        contact.set_contact({"Name":name,"Phone":phone,"Email":email})
        pb.update_contact(contact,name)
    elif choice == 6:
        print("Programe exiting...")
        break
    else :
        print("invalid choice programe exiting...")
        break 
    
