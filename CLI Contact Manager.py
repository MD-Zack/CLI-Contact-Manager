import os
import json

# Define the filename for storing contacts
database_file = "contact.json"

def load_database():
    """
    Loads the contact list from the JSON database file.
    If the file does not exist, it initializes the file with an empty list.
    Handles JSON decode errors by returning an empty list, ensuring robustness.

    Returns:
        list: List of contact dictionaries.
    """
    if not os.path.exists(database_file):
        # Initialize an empty JSON file if it doesn't exist
        with open(database_file, "w") as write_file:
            json.dump([], write_file, indent=4)
            print("Database file created successfully.\n")

    with open(database_file, "r") as read_file:
        try:
            data = json.load(read_file)
            return data
        except json.JSONDecodeError:
            # If the file is corrupted or empty, return empty list
            return []

def save_contact(data):
    """
    Persists the contact list to the JSON database file.

    Args:
        data (list): List of contact dictionaries to save.
    """
    with open(database_file, "w") as write_file:
        json.dump(data, write_file, indent=4)

def add_contact(fname, lname, phone_number):
    """
    Adds a new contact record to the database and saves it.

    Args:
        fname (str): First name of the contact.
        lname (str): Last name of the contact.
        phone_number (str): Phone number of the contact.
    """
    data = load_database()
    new_contact = {
        "FirstName": fname,
        "LastName": lname,
        "PhoneNumber": phone_number
    }
    data.append(new_contact)
    save_contact(data)

def search(keyword):
    """
    Searches for contacts whose last names contain the given keyword (case-insensitive).

    Args:
        keyword (str): Substring to search in last names.

    Prints matching contacts or a message if none found.
    """
    data = load_database()
    results = [contact for contact in data if keyword.lower() in contact["LastName"].lower()]
    if results:
        for contact in results:
            print(f"First Name: {contact['FirstName']}, Last Name: {contact['LastName']}, Phone: {contact['PhoneNumber']}")
    else:
        print("No contacts found with the specified last name.")

def delete(keyword):
    """
    Deletes all contacts whose last names match the given keyword (case-insensitive).

    Args:
        keyword (str): Last name to delete.

    Saves updated contact list after deletion.
    """
    data = load_database()
    filtered_contacts = [contact for contact in data if contact['LastName'].lower() != keyword.lower()]
    save_contact(filtered_contacts)

def show_database():
    """
    Displays all contacts currently stored in the database.
    If no contacts are stored, informs the user accordingly.
    """
    data = load_database()
    if not data:
        print("No contacts found in the database.")
    else:
        print("Contacts list:")
        for contact in data:
            print(f"First Name: {contact['FirstName']}, Last Name: {contact['LastName']}, Phone: {contact['PhoneNumber']}")

def main():
    """
    The main interactive loop presenting the user with a menu to manage contacts.
    Handles user input and routes to the corresponding functionality.
    Continues until the user chooses to exit.
    """
    while True:
        print('''
        ================================
        1. Add contact
        2. Search contact by Last Name
        3. Delete contact by Last Name
        4. Show all contacts
        5. Exit
        ================================
        ''')
        
        choice = input("Enter your choice number: ").strip()

        if choice == "1":
            fname = input("Enter First Name: ").strip()
            lname = input("Enter Last Name: ").strip()
            phone_number = input("Enter Phone Number: ").strip()
            add_contact(fname, lname, phone_number)
            print("Contact added successfully!")

        elif choice == "2":
            keyword = input("Enter Last Name to search: ").strip()
            search(keyword)

        elif choice == "3":
            keyword = input("Enter Last Name to delete: ").strip()
            delete(keyword)
            print("Contact(s) deleted successfully!")

        elif choice == "4":
            show_database()

        elif choice == "5":
            print("Thank you for using Simple Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
