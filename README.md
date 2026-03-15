# Python Expense Tracker (CLI)

## Overview

This is a terminal-based Expense Tracker built using Python.
The program allows users to record expenses and analyze their spending directly from the command line.

The application demonstrates core Python programming concepts such as:

* Classes (Object-Oriented Programming)
* Lists and dictionaries
* Functions
* Loops and conditionals
* Basic data analysis logic

The entire system runs in a single Python file and stores expenses in memory during runtime.

---

## Features

* Add new expenses
* View total expenses
* Analyze spending by category
* Find the most expensive purchase
* Calculate average expense
* Menu-driven command line interface

---

## Project Structure

```
expense-tracker/
│
├── expense_tracker.py
├── README.md
├── .gitignore
└── LICENSE
```

---

## How It Works

Each expense is stored as an object using a Python class.

Example expense data:

```
item: Lunch
category: Food
amount: 120
```

These objects are stored in a list and analyzed using Python functions.

---

## How to Run the Project

1. Clone the repository

```
git clone https://github.com/yourusername/expense-tracker.git
```

2. Navigate into the project folder

```
cd expense-tracker
```

3. Run the program

```
python expense_tracker.py
```

---

## Example Menu

```
1. Add New Expense
2. Show Total Expenses
3. Spending by Category
4. Most Expensive Purchase
5. Average Expense
6. Exit
```

---

## Example Output

```
Item - Lunch | Price - 120
Item - Bus | Price - 40

Your total expenditure is: 160
```

---

## Concepts Demonstrated

This project practices several important Python concepts:

* Object-Oriented Programming
* Data storage using lists
* Dictionary aggregation
* Lambda functions
* Built-in functions like `max()` and `len()`
* Command-line interface design

---

## Future Improvements

Possible improvements for this project include:

* Save expenses to a file (JSON or CSV)
* Load expenses when the program starts
* Monthly spending reports
* Expense search functionality
* Data visualization

---

## Author

Created as a learning project to practice Python fundamentals and build small real-world applications.
