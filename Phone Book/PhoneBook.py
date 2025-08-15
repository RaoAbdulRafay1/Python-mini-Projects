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
pb= PhoneBook()
pb.add_contact({"Rao" : "033333333"})
pb.add_contact({"Rao1" : "032333333"})
pb.add_contact({"Rao2" : "035333333"})                     
pb.display_contacts()
print("Search ")
pb.search_contact("Rao1")

pb.delete_contact("Rao")
pb.display_contacts()


