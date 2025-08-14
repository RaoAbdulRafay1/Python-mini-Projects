class PhoneBook :
    def __init__(self):
       self.contacts = []
    def add_contact(self,contact):
        self.contacts.append(contact)
        print(f"Contact {contact} was added")
    def display_contacts(self):
        for i in self.contacts :
            print(i)
            

pb =PhoneBook()
pb.add_contact({"Abdul Rafay" : "033312125523"})
pb.add_contact({"Ansar" : "0333212121"})
pb.add_contact({"Abdul" : "033452783"})
pb.display_contacts()



        
         



