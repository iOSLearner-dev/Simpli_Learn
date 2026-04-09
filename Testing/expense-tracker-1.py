import os
import csv

# CSV File Path in System.
EXPENSES_CSV_PATH = os.path.expanduser("~/Documents/LearningWorkSpace/SL-Learning/Chapter-1-Python/expenses.csv")

# expenses
expenses = []

# Monthly Budget
monthly_budget = 0.0

# Add Expense
def add_expense():
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the category: ")
    amount = float(input("Enter the amount: ")) 
    description = input("Enter a description: ")

    # Store as a dictionary
    expense = {
        'date': date,
        'category': category,
        'amount': amount,
        'description': description
    }
    expenses.append(expense)
    print("Expense added successfully!")

# View Expenses
def view_expenses():
    if not expenses:
        print("\nNo expenses recorded yet.")
        return

    print("\n--- All Expenses ---")
    for expense in expenses:
        # Validate data: check if all keys exist and have values
        if all(key in expense for key in ["date", "category", "amount", "description"]):
            print(f"{expense['date']} | {expense['category']} | ${expense['amount']:.2f} | {expense['description']}")
        else:
            print("Skipping incomplete entry.")

# Set and Track Budget
# 1. Set Budget
def set_budget():
    """
    Get monthly budget amount from the user.
    """
    # TODO: Ask for input, convert to float, return it
    budget = float(input("Enter your monthly budget: $"))
    return budget

# 2. Track Budget
def track_budget(expenses, budget):
    """
    Compare total spending to the budget.
    """
    # Sum up all expense amounts
    total_expenses = sum(expense['amount'] for expense in expenses if 'amount' in expense)

    # Compare with budget
    if total_expenses > budget:
        print("You have exceeded your budget!")
    else:
        remaining = budget - total_expenses
        print(f"You have ${remaining:.2f} left for the month.")


# Save and Load Expense
# 1.Save Expenses
def save_expenses(filename=EXPENSES_CSV_PATH):
    """
    Save expenses to a CSV file.
    """
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Amount", "Description"])

        for expense in expenses:
            writer.writerow([expense.get("date"), expense.get("category"), expense.get("amount"), expense.get("description")])

# 2. Load Expenses
def load_expenses(filename=EXPENSES_CSV_PATH):
    """
    Load expenses from CSV file into a list.
    """
    expenses = []

    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row.get("amount"):
                    row["amount"] = float(row["amount"])
                expenses.append(row)
    except FileNotFoundError:
        print(f"File not found: {filename}")
    except Exception as e:
        print(f"An error occurred while loading expenses: {e}")

    return expenses

# User Menu
def main():
    """
    Main interactive menu for the user.
    """
    global expenses, monthly_budget

    # Load existing expenses from file
    expenses = load_expenses()

    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Set Budget")
        print("4. Track Budget")
        print("5. Save and Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            monthly_budget = set_budget()
        elif choice == '4':
            track_budget(expenses, monthly_budget)
        elif choice == '5':
            save_expenses()
            print("Expenses saved. Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Start of program
if __name__ == "__main__":
    main()