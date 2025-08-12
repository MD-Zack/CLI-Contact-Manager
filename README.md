# CLI-Contact-Manager

A simple command-line contact book application written in Python.  
This program allows users to add, search, delete, and list contacts stored in a JSON file.  

## Features (Version 1.0)

- Add new contacts (First Name, Last Name, Phone Number)  
- Search contacts by Last Name  
- Delete contacts by Last Name  
- Show all saved contacts  
- Data persistence using JSON file  

## How to Run

1. Make sure you have Python 3 installed on your system.  
2. Clone this repository or download the `contact_book.py` file.  
3. Run the program:  
   python contact_book.py
Follow the on-screen menu to use the features.

Future Updates (Planned Features)
Input validation and improved error handling

Edit existing contacts

Search by other fields (First Name, Phone Number)

Support for multiple phone numbers per contact

Sorting and pagination of contacts

Export/import contacts to/from CSV or other formats

GUI version for better user experience

Code Structure and Comments
The code is organized into modular functions with clear responsibilities:

load_database() — loads or initializes the JSON database

save_contact(data) — saves the current contact list to the file

add_contact(fname, lname, phone_number) — adds a new contact

search(keyword) — searches contacts by last name

delete(keyword) — deletes contacts by last name

show_database() — prints all contacts

main() — runs the interactive menu loop

Comments are included in the code for clarity and easy maintenance.

```bash
