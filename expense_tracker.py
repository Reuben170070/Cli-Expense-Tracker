#Name: Reuben Aby
#Project name: Expense Tracker
#Date: May 4th 2025
#Description : A command-line application to track expenses, allowing users 
            #to add, view, and categorize expenses (e.g., food, travel) with a summary of total spending. 


import datetime
import json
import os

#Load expenses from JSON file
def load_expenses():
    try:
        with open("expenses.json", "r" ) as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return[]

#initializing expenses list
expenses = []

#script to display a menu and handle user input in a loop. 

#displaying the menu to the user
def display_menu():
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Summary")
    print("4. Exit")

#TheExpenseFunction

def add_expense():
    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print("Amount must be positive.")
            return
        category = input("Enter category (e.g., food, travel): ").strip().lower()
        if not category:
            print("Category cannot be empty.")
            return
        date = input("Enter date (YYYY-MM-DD, or press Enter for today): ").strip()
        if not date:
            date = datetime.datetime.today().strftime("%Y-%m-%d")
        else:
            try:
                datetime.datetime.strptime(date, "%Y-%m-%d")
            except ValueError:
                print("Invalid date format. Use YYYY-MM-DD.")
                return
        expenses.append({"amount" : amount, "category" : category, "date": date})
        print("Expense added successfully!")
    except ValueError:
            print("Invalid amount. Please enter a number.")

#Displaying the expenses
def view_expenses():
    if not expenses:
        print("No expenses recorded.")
        return
    print("\nAll Expenses:")
    for i, expense in enumerate(expenses, 1):
        print(f"{i}. Amount: ${expense['amount']:.2f} , Category: {expense['category']}, Date: {expense['date']}")

#Summary function 
#Function to calculate and display the total spent and a breakdown by category. 

def view_summary():
    if not expenses:
        print("No expenses to summarize.")
        return
    total_spent = sum(expense["amount"] for expense in expenses)
    category_totals = {}
    for expense in expenses:
        category = expense["category"]
        category_totals[category] = category_totals.get(category, 0) + expense["amount"]
        

    print(f"\nTotal Spent: ${total_spent:.2f}")
    print("Breakdown by Category:")
    for category, total in category_totals.items():
        print(f"{category}: ${total:.2f}")


#function to check menu selected by user
def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")
        os.system("clear") #Clear screen after input
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            view_summary()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
        input("Press Enter to continue...") #Pause before redisplaying menu
        

if __name__ == "__main__":
    main()
