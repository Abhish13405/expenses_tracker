# expenses_tracker
# Personal Expense Tracker (CLI Based)

This is a simple command line based Personal Expense Tracker project built using Python.

## About the Project

This project helps users to manage their daily expenses from the terminal.  
It stores the expense records in a text file and allows basic operations like adding, viewing, deleting, and filtering expenses.

The main goal of this project was to understand file handling and basic backend logic in Python.

## Features

- Add new expense
- View all expenses
- Filter expenses by date or category
- Delete an expense
- Monthly summary (total and category-wise)

## Technologies Used

- Python
- File Handling
- Datetime module
- Basic CLI interaction

## How It Works

When the program runs, it creates a file named `expenses.txt` (if it does not already exist).

All expense data is stored in this format:

Date, Amount, Category, Description

The program uses Functions for each operation and a loop-based menu system to allow user interaction.

## Learning Outcome

through this project, I learned:

- How to work with files in Python
- How to handle user input
- Basic CRUD operations
- Working with date and time
- Organizing code using functions

# Future Improvements

In the Future, I would like to:

- Add input validation and exception handling
- Convert this project into a web-based application using Flask
- Integrate MySQL database instead of text file storage
