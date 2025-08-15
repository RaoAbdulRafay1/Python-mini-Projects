class PhoneBook :
    def __init__(self):
       self.contacts = []
    def add_contact(self,contact):
        self.contacts.append(contact)
        print(f"Contact {contact} was added")
    def display_contacts(self):
        for i in self.contacts :
            print(i)
    def search_contact(self,name):
        for contact in self.contacts:
            if name in contact:
                print(f"Found contact  {contact} .")
    def delete_contact(self,name):
        for contact in self.contacts:
            if name in contact:
                self.contacts.remove(contact)
                print(f"{contact} was deleted")
    def update_contact(self,cont,name):
        for i, contact in enumerate(self.contacts):
            if contact["name"] == name:
                self.contacts[i] = cont
                print(f"{cont} was updated")
pb= PhoneBook()
pb.add_contact({"name": "Rao" , "phone": "033333333"})
pb.add_contact({"name": "Rao1" , "phone": "032333333"})
pb.add_contact({"name": "Rao2" , "phone": "035333333"})
pb.display_contacts()
print("Search ")
pb.search_contact("Rao1")

pb.delete_contact("Rao")
pb.display_contacts()
pb.update_contact({"name":"Rao","phone":"23111231"},"Rao")
print("After update")
pb.display_contacts()

