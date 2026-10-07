import csv
import os

FILE_NAME = "expenses.csv"


def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Description", "Amount"])


def add_expense():
    print("\n===== ADD EXPENSE =====")

    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category: ")
    description = input("Enter description: ")

    while True:
        try:
            amount = float(input("Enter amount: "))

            if amount <= 0:
                print("Amount must be greater than 0.")
                continue

            break

        except ValueError:
            print("Invalid amount. Please enter a number.")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])

    print("Expense added successfully!")


def view_expenses():
    print("\n===== ALL EXPENSES =====")

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        expenses = list(reader)

        if not expenses:
            print("No expenses found.")
            return

        print("\nDate\t\tCategory\tDescription\tAmount")
        print("-" * 65)

        for expense in expenses:
            print(
                f"{expense['Date']}\t"
                f"{expense['Category']}\t\t"
                f"{expense['Description']}\t"
                f"₹{expense['Amount']}"
            )


def filter_expenses():
    print("\n===== FILTER EXPENSES =====")

    category = input("Enter category to filter: ").lower()

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        found = False

        for expense in reader:
            if expense["Category"].lower() == category:
                print(
                    f"{expense['Date']} | "
                    f"{expense['Category']} | "
                    f"{expense['Description']} | "
                    f"₹{expense['Amount']}"
                )
                found = True

        if not found:
            print("No expenses found for this category.")


def category_summary():
    print("\n===== CATEGORY SUMMARY =====")

    summary = {}

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for expense in reader:
            category = expense["Category"]

            amount = float(expense["Amount"])

            if category in summary:
                summary[category] += amount
            else:
                summary[category] = amount

    if not summary:
        print("No expenses available.")
        return

    for category, total in summary.items():
        print(f"{category}: ₹{total:.2f}")


def main():
    initialize_file()

    while True:
        print("\n==============================")
        print("     PERSONAL EXPENSE TRACKER")
        print("==============================")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Filter Expenses")
        print("4. Category Summary")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            filter_expenses()

        elif choice == "4":
            category_summary()

        elif choice == "5":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice! Please select 1-5.")


main()