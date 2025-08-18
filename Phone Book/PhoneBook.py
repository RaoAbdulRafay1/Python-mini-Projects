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
            if name in contact:
                print(f"Found contact  {contact.get_contact()} .")
    def delete_contact(self,name):
        for contact in self.contacts:
            if name in contact:
                self.contacts.remove(contact)
                print(f"{contact.get_contact()} was deleted")
    def update_contact(self,cont,name):
        for contact in self.contacts:
            if name in contact:
                self.contacts.remove(contact)
                self.contacts.append(cont)
                print(f"{contact.get_contact()} was updated to {cont.get_contact()}")
pb= PhoneBook()
print("Enter name,phone and email")
name =input("Name :")
phone = input("Phone :")
email = input("Email:")
c =Contact()
c.set_contact({"Name":name,"Phone":phone,"Email":email})


pb.add_contact(c)
pb.display_contacts()