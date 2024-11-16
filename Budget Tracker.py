# Budget Tracker (Without using functions or imports)

# Starting budget amount
budget = float(input("Enter your starting budget amount: "))

# Track expenses and categories
expenses = []

# Categories for expenses
categories = ["Food", "Transport", "Entertainment", "Bills", "Others"]

# Start the tracker
print("\nWelcome to your Budget Tracker!")

# Main tracker loop
while True:
    # Show current budget and expenses
    print("\nCurrent Budget: $", round(budget, 2))
    print("\nExpenses so far:")
    
    if expenses:
        for expense in expenses:
            print(f"Category: {expense[0]}, Amount: ${round(expense[1], 2)}")
    else:
        print("No expenses recorded yet.")
    
    print("\nCategories:")
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")
    print("Enter '0' to exit and view the summary.")
    
    # Ask user to input an expense or exit
    choice = input("\nSelect a category number to add an expense or '0' to exit: ")
    
    if choice == '0':
        break
    
    # Check if choice is valid
    if choice.isdigit() and 1 <= int(choice) <= len(categories):
        category = categories[int(choice) - 1]
        expense_amount = input(f"Enter the amount for {category}: $")
        
        if expense_amount.replace('.', '', 1).isdigit():  # Check if the amount is a valid number
            expense_amount = float(expense_amount)
            if expense_amount <= budget:
                budget -= expense_amount
                expenses.append([category, expense_amount])
                print(f"Expense of ${round(expense_amount, 2)} added to {category}.")
            else:
                print(f"You don't have enough budget for that expense. Your remaining budget is: ${round(budget, 2)}")
        else:
            print("Invalid amount. Please enter a valid number.")
    else:
        print("Invalid choice. Please select a valid category.")

# Show the final summary
print("\n--- Final Budget Summary ---")
print(f"Starting Budget: ${round(float(input('Enter your starting budget amount: ')),2)}")
print("Expenses:")
for expense in expenses:
    print(f"Category: {expense[0]}, Amount: ${round(expense[1], 2)}")

print("\nRemaining Budget: $", round(budget, 2))
