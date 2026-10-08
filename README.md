# Personal Knowledge Management System

A Python-based command-line application for creating, accessing, modifying, and managing personal notes. The project is designed using Object-Oriented Programming (OOP) concepts.

## Features

- User login with username and password validation
- Add personal notes with topics
- Access notes using topic names
- Modify existing notes
- User logout functionality
- Login verification before accessing note features
- Simple menu-driven command-line interface

## Technologies Used

- Python
- Object-Oriented Programming (OOP)

## OOP Concepts Used

- Class and Object
- Constructor (`__init__`)
- Instance attributes
- Instance methods
- Conditional statements and loops
- Dictionaries and lists

## Project Structure

```text
PKM1/
│
├── main.py
└── README.md
```

## How It Works

The application provides a menu with the following options:

1. **Login** – Enter a username and password to log in.
2. **Add Note** – Create a note using a topic and its content.
3. **Access Note** – Retrieve a note using its topic.
4. **Modify Note** – Update the content of an existing note.
5. **Logout** – Log out the currently logged-in user.

Users must log in before they can add, access, or modify notes.

## How to Run

Make sure Python is installed on your system.

Clone the repository and open the project folder in VS Code or a terminal.

Run:

```bash
python main.py
```

Follow the instructions displayed in the terminal.

## Example
======================PERSONAL KNOWLEDGE MANAGEMENT SYSTEM======================
1.Login
2.Add Note
3.Access Note
4.Modify Note
5.Logout
Enter your Choice : 1
Enter the valid Username : Vani
Username should  contain special characters
======================PERSONAL KNOWLEDGE MANAGEMENT SYSTEM======================
1.Login
2.Add Note
3.Access Note
4.Modify Note
5.Logout
Enter your Choice : Vani@
Invalid choice
======================PERSONAL KNOWLEDGE MANAGEMENT SYSTEM======================
1.Login
2.Add Note
3.Access Note
4.Modify Note
5.Logout
Enter your Choice : 1
Enter the valid Username : Vani@
Enter the Password : Vani@1234
Login Successful

## Future Improvements

- Add delete note functionality
- Store notes permanently using files or a database
- Improve user authentication
- Allow multiple users to have separate notes
- Add note search functionality
- Add a graphical or web-based interface

## Author

Y Vani

GitHub: https://github.com/yellavani15
