import calendar
import datetime
from expense import Expense


def main():

    
    print(f"running expense")
    expense_file_path = 'expenses.csv'
    budget = 2000

   
    # Get user input for expense
    
    expense = get_user_expense()
    
    # Write their expense into a file.
    save_expense_to_file(expense, expense_file_path)

    # Read the file and summarize expenses.
    summarize_user_expense(expense_file_path, budget)

    
 

def get_user_expense():
    print(f" Get user expense")
    expense_name = input('Enter expense name: ')
    expense_amount = float(input('Enter expense amount: '))
   


    expense_categories = [
        'Food', 'Home', 'Work', 'Fun', 'Misc'
    ]

    while True:
        print("Select a category: ")
        #Loops to show how many categories we previously defined
        for i, category_name in enumerate(expense_categories):
            print(f"  {i + 1}. {category_name}")


        #variable for storing categories 
        value_range = f"[1 - {len(expense_categories)}]"
      

        #Gets user input on what category number to choose
        selected_index = int(input(f"Enter a category number {value_range}: ")) - 1 


        #checks if user input is within the expense category length

        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(
                name=expense_name, category=selected_category, amount=expense_amount
            )
            return new_expense
        

        else:
            print("Invalid Category. Please Try again!")


        
     

def save_expense_to_file(expense: Expense, expense_file_path):
    print(f" Save user expense: {expense} to {expense_file_path}")
    with open(expense_file_path, 'a') as f:
        f.write(f'{expense.name},{expense.amount},{expense.category}\n')
    

def summarize_user_expense(expense_file_path, budget):
    print(f" Summarize user expense")
    expenses: list[Expense] = []
    with open(expense_file_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            stripped_line = line.strip()
            expense_name, expense_amount, expense_category = stripped_line.split(',')
            line_expense = Expense(name=expense_name, amount=float(expense_amount), category=expense_category)

            print(line_expense)
            expenses.append(line_expense)
        
    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] += expense.amount

    print("Expenses by Category: ")
    for key, amount in amount_by_category.items():
        print(f" {key}: ${amount:.2f}")

    total_spent = sum([ex.amount for ex in expenses])
    print(f" You've spent ${total_spent:.2f} this month!")
    
    remaining_budget = budget - total_spent
    print(f" Budget Remaining: ${remaining_budget:.2f}")


    #Get the current date
    now = datetime.datetime.now()

    # Get the number of days in the current month
    days_in_month = calendar.monthrange(now.year, now.month)[1]

    # Calculate the remaining number of days in the current month
    remaining_days = days_in_month - now.day

    daily_budget = remaining_budget / remaining_days
    print(f' Budget per Day: ${daily_budget:.2f}')

    

if __name__ == "__main__":
    main() 
