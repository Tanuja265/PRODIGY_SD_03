import json
class ContactManager:
    def __init__(self, storage_file='contacts.json'):
        self.contacts = []
        self.storage_file = storage_file
        self.load_contacts()
    def load_contacts(self):
        try:
            with open(self.storage_file, 'r') as file:
                self.contacts = json.load(file)
        except FileNotFoundError:
            self.contacts = []
    def save_contacts(self):
        with open(self.storage_file, 'w') as file:
            json.dump(self.contacts, file, indent=4)
    def add_contact(self, name, phone, email):
        new_contact = {'name': name, 'phone': phone, 'email': email}
        self.contacts.append(new_contact)
        self.save_contacts()
    def view_contacts(self):
        for idx, contact in enumerate(self.contacts, start=1):
            print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    def edit_contact(self, index, name=None, phone=None, email=None):
        if 0 <= index < len(self.contacts):
            if name:
                self.contacts[index]['name'] = name
            if phone:
                self.contacts[index]['phone'] = phone
            if email:
                self.contacts[index]['email'] = email
            self.save_contacts()
        else:
            print("Invalid contact index.")
    def delete_contact(self, index):
        if 0 <= index < len(self.contacts):
            self.contacts.pop(index)
            self.save_contacts()
        else:
            print("Invalid contact index.")
def main():
    manager = ContactManager()
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            manager.add_contact(name, phone, email)
        elif choice == '2':
            manager.view_contacts()
        elif choice == '3':
            manager.view_contacts()
            index = int(input("Enter the contact number to edit: ")) - 1
            name = input("Enter new name (leave blank to keep current): ")
            phone = input("Enter new phone (leave blank to keep current): ")
            email = input("Enter new email (leave blank to keep current): ")
            manager.edit_contact(index, name or None, phone or None, email or None)
        elif choice == '4':
            manager.view_contacts()
            index = int(input("Enter the contact number to delete: ")) - 1
            manager.delete_contact(index)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == '__main__':
    main()