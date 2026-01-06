expenses = []

def add_expense():
    item = input("Enter expense item: ")
    amount = input("Enter amount: ")
    expenses.append({"item": item, "amount": amount})
    print("Expense added")

def view_expenses():
    if not expenses:
        print("No expenses recorded")
    else:
        for expense in expenses:
            print(expense["item"], "-", expense["amount"])

def main():
    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            break
        else:
            print("Invalid option")

main()
