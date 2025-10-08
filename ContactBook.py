# Goal: Develop a command-line application to manage a list of contacts.

# Requirements:

# Use a dictionary to store contact information. The key should be the contact's name, and the value should be another dictionary containing their phone number and email address.
# Use functions to encapsulate the following actions:

# Add a new contact.
# View all contacts.
# Search for a contact by name.
# Remove a contact.
# The program should have a main loop that presents a menu of options (add, view, search, remove, exit) to the user.
# NOTE: You may use a Class to handle the contact book

class ContactBook: #TODO: Polish the whole thing up and its good to go!!!!

    def __init__(self):
        self.contacts = {} # Dict will work as a list as well 

    def add_contact(self, name, number, email): # Have to add these variables to be able to append them (update: We cant append dicts, only list!!!)
        # If no name is given the below line will be used
        if not name.strip():
            print("No names were entered!")
            return
        
        # If no number is given the below line will be used
        if not number.isdigit():
            print("A number was not given")
            return
        
        # Error handling if no @ is given 
        if "@" not in email:
            print("An email was not given")
            return
        
        self.contacts[name] = {'Phone: ': number, 'Email: ': email}
        print("Contact was added!")
    
    def view_all_contacts(self):
        for name, info in self.contacts.items():
            print(f"Name: {name} Phone: {info['Phone: ']} Email: {info['Email: ']}")
    
    def contact_search(self,name):
        if name in self.contacts:
            print(f"Phone: {self.contacts[name]['Phone: ']} Email: {self.contacts[name]['Email: ']}")
        else:
            print("There isnt such a name in your contacts")

    def remove_contact(self,name): 
        if name in self.contacts:
            del self.contacts[name]
            print(f"{name} has been removed")
        else:
            print("Nobody with that name exists")

book = ContactBook()

while True:

    print("\n--Contact Book--\n")
    print("1. Add contact")
    print("2. Search contact")
    print("3. View all contacts")
    print("4. Update contact")
    print("5. Remove contact")
    print("6. Exit")

    option = input("\nChoose an option by entering the number next to it ")

    # Add contact
    if option == "1":
        name = input("Name: ")
        number = input("Number: ")
        email = input("Email: ")
        book.add_contact(name,number,email)

    # Search contact
    elif option == "2":
        name = input("Who are we searching for?: ")
        book.contact_search(name)

    # View all contacts
    elif option == "3":
        book.view_all_contacts()

    # Updating the contact
    elif option == "4": # TODO: A lot of polish
        name = input("Which contact do you want to update? ")
        update_choice = input("Do you want to update number, email or both? ")
        if update_choice == "both":
            new_number = input("Type in the new number: ")
            new_email = input("Type in the new email adress: ")
            book.contacts[name]["Phone: "] = new_number
            book.contacts[name]["Email: "] = new_email
        elif update_choice == "number":
            new_number = input("Type in the new number: ")
            print("New number registered!")
        elif update_choice == "email":
            new_email = input("Type in the new email adress: ")
            print("New email adress registered!")
        
    # Delete contact
    elif option == "5":
        name = input("What contact would you like to remove? ")
        book.remove_contact(name)

    # Exit the contact book
    elif option == "6":
        print("The contact book is now closed!")
        break



