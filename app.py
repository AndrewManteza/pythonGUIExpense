


#Should I give the user a choice wether to have the income as monthly or yearly
 

# App requirements:
# User enters expense
# Save expense to CSV file
# Summarise expense totals 
# Show remaining budget

 
def user_inputFunction():
    initialCash = 0
    total_income = 0
    total_expense = 0
    user_dict = {} 

    overallIncome = int(input("how much do you earn month after taxes:"))
    overallExpense = int(input("how much do you earn month after taxes:"))


    addExpense = int(input("How many expense categories do you want to make? "))
    
    # This is the for loop for the user entry as dictionary
    for i in range(addExpense):
        key = input("Enter Type of Expense: ")
        value = input("Enter How much that Expense is: ")
        user_dict[key] = value

    print("Here is a list of all your expenses", user_dict)

    


    print(overallIncome - overallExpense)

    


user_inputFunction()
   

    
    
     


    
















