def add_expenses(expenses, description, amount):
    expenses.append({"description":description, "amount": amount})
    print(f"Added Expense : {description}, Amount : {amount}")

def get_total_expenses(expenses):
    sum = 0
    for expense in expenses:
        sum += expense['amount']
    return sum

def get_balance(budget, expenses):
    return budget - get_total_expenses(expenses)

def show_budget_details(budget, expenses):
    print(f"Total Budget : {budget}")
    print("Expenses")
    for expense in expenses:
        print(f" - {expense['description']}: {expense['amount']}")
    print(f"Total Expenses : {get_total_expenses(expenses)}")
    print(f"Remaining Budget : {get_balance(budget, expenses)}")
                     

def main():
    print("Welcome to Budget Tracker App")
    initial_budget = float(input("Please enter your initial budget : "))
    budget = initial_budget
    expenses = []
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Add your expense")
        print("2. Show Budget Details")
        print("3. Exit")
        choice = int(input("Enter your Choice : "))
        
        if choice == 1:
            description = input("Enter expense Description : ")
            amount = float(input("Enter expenses amount : "))
            add_expenses(expenses, description, amount)
            
        elif choice == 2:
            show_budget_details(budget, expenses)
        
        elif choice == 3:
            print("Thanks for Visiting...")
            break
        
        else:
            print("Please enter the correct choice")

if __name__ == "__main__":
    main()