def main():

    print(f"running expense")


   
    # Get user input for expense
    get_user_expense()

    # Write their expense into a file.
    save_user_expense()

    # Read the file and summarize expenses.
    summarize_user_expense()

    


def get_user_expense():
    print(f" Get user expense")
    expense_name = input('Enter expense name: ')
    expense_amount = float(input('Enter expense amount: '))
    print(f"You have entered {expense_name}. {expense_amount}")


    expense_categories = [
        'Food', 'Home', 'Work', 'Fun', 'Misc'
    ]

    while True:
        print('Select a category: ' )
        #Loops to show how many categories we previously defined
        for i, category_name in enumerate(expense_categories):
            print(f' {i + 1}, {category_name}')


        #variable for storing categories 
        value_range = f"[1 - {len(expense_categories)}]"


        #Gets user input on what category number to choose
        selected_index = int(input(f"Enter a category number: {value_range}: ")) -1 


        #checks if user input is within the expense category length

        if selected_index in range(len(expense_categories)):
            break
        else:
            print("Invalid Category. Please Try again!")


            
    

def save_user_expense():
    print(f" Save user expense")
   

def summarize_user_expense():
    print(f" Summarize user expense")
   



if __name__ == "__main__":
    main()