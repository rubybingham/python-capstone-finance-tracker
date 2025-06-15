def add_expense():
    try:
        desc = input("Enter expense description: ")
        category = input("Enter category: ")
        amount = float(input("Enter amount: "))
        if category not in data:
            data[category] = []
        data[category].append((desc, amount))
    except ValueError:
        print("Please enter a valid input.")
    else:
        print("Expense added successfully.")


def view_expenses():
    if not data:
        print("No expenses recorded yet.")
        return
    for category, expense_list in data.items():
        print(f"Category: {category}")
        for description, amount in expense_list:
            print(f"  - {description}: ${amount}")


def view_summary():
    if not data:
        print("No expenses recorded yet.")
        return

    total_expenses = {}
    for category, expense_list in data.items():
        total_amount = sum(amount for _, amount in expense_list)
        total_expenses[category] = total_amount

    print("Expense Summary:")
    for category, total in total_expenses.items():
        print(f"  - {category}: ${total}")


def display_menu():
    print("What do you want to do? ")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Summary")
    print("4. Exit")

print("Welcome to the Personal Finance Tracker!")
data = {}
while True:
    display_menu()
    choice = input("Choose an option: ")
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        view_summary()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
