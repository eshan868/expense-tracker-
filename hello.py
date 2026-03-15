# -------- MENU FUNCTION --------
# Displays the options available to the user
def menu():
    print("\n====== Expense Tracker ======")
    print("1. Add New Expense")
    print("2. Show Total Expenses")
    print("3. Spending by Category")
    print("4. Most Expensive Purchase")
    print("5. Average Expense")
    print("6. Exit")


# -------- EXPENSE CLASS --------
# This class represents one expense item
class Expense:
    def __init__(self, item, category, amount):
        self.item = item        # name of the item
        self.category = category # category of expense
        self.amount = amount     # price of the item


# -------- GLOBAL STORAGE --------
# List to store all expense objects
expense_data = []


# -------- ADD NEW EXPENSE --------
def add_new_expense():
    item = input("Enter the item: ")
    category = input("Enter the category: ")
    amount = float(input("Enter the price: "))

    # Create an Expense object
    expense = Expense(item, category, amount)

    # Store it in the list
    expense_data.append(expense)

    print("Expense added successfully!")


# -------- TOTAL EXPENSE --------
def total_expense():

    # If no expenses exist
    if len(expense_data) == 0:
        print("No expenses added yet.")
        return 0

    total = 0

    # Loop through each expense
    for expense in expense_data:
        total += expense.amount
        print(f"Item - {expense.item} | Price - {expense.amount}")

    print(f"\nYour total expenditure is: {total}")

    # Return total so other functions can use it
    return total


# -------- SPENDING BY CATEGORY --------
def spending_by_category():

    if len(expense_data) == 0:
        print("No expenses available.")
        return

    # Create dictionary to store totals
    category_total = {}

    for expense in expense_data:

        category = expense.category
        amount = expense.amount

        # If category appears first time
        if category not in category_total:
            category_total[category] = amount

        # If category already exists, add to it
        else:
            category_total[category] += amount

    print("\nSpending by Category:")
    for category, total in category_total.items():
        print(f"{category} : {total}")


# -------- MOST EXPENSIVE PURCHASE --------
def most_expensive_purchase():

    if len(expense_data) == 0:
        print("No expenses available.")
        return

    # Find object with highest amount
    most_expensive = max(expense_data, key=lambda expense: expense.amount)

    print(f"Most expensive purchase is: {most_expensive.item} - {most_expensive.amount}")


# -------- AVERAGE EXPENSE --------
def average_purchase():

    if len(expense_data) == 0:
        print("No expenses available.")
        return

    # Get total from the function
    total = total_expense()

    # Count number of expenses
    total_items = len(expense_data)

    # Calculate average
    average_expense = total / total_items

    print(f"\nYour average expense is: {average_expense}")


# -------- MAIN PROGRAM LOOP --------
while True:

    menu()

    try:
        user_choice = int(input("Enter the number based on the selection: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if user_choice == 1:
        add_new_expense()

    elif user_choice == 2:
        total_expense()

    elif user_choice == 3:
        spending_by_category()

    elif user_choice == 4:
        most_expensive_purchase()

    elif user_choice == 5:
        average_purchase()

    elif user_choice == 6:
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid option. Try again.")