# Print a welcome message
print("Welcome to the Personal Finance Tracker")

#Create empty lists to store income and expenses
income = []
expenses = []

#Check income and expense input is to two decimal places
def validate_less_than_2_dp(number: str):
  split_entry = number.rsplit('.')
  decimal_present = len(split_entry)==2
  if decimal_present:
    num_decimals = len(split_entry[1])
    too_many_decimals = num_decimals > 2
  else:
    too_many_decimals = False
    
  return too_many_decimals
    
# Main loop for the Personal Finance Tracker program
while True:
  
  #Prompt the user to choose an action - Menu
  action= input("Please choose from the following options: \n1. Add an income \n2. Add an expense \n3. View financial summary \n4. Quit \nEnter your choice: ")
  
  #Add an income item
  if action== '1':
    awaiting_number_2d = True
    while awaiting_number_2d:
      income_entry=input("Enter the income amount to two decimal places: ")
      too_many_decimals = validate_less_than_2_dp(number=income_entry)
      if too_many_decimals:
        print("Income amount must be to two decimal places.")
      else:
       awaiting_number_2d = False
    income.append(float(income_entry))
    print("Income added successfully")
    
  #Add an expense
  elif action == '2':
    awaiting_number_2d = True
    while awaiting_number_2d:
      expense_entry= input("Enter an expense to two decimal places: ")
      too_many_decimals = validate_less_than_2_dp(number=expense_entry)
      if too_many_decimals:
        print("Expense amount must be to two decimal places.")
      else:
        awaiting_number_2d = False
    expenses.append(float(expense_entry))
    print("Expense added successfully")
    
  #View a financial summary
  elif action == '3':
    total_income = sum(income)
    total_expenses = sum(expenses)
    remaining_balance = total_income-total_expenses
    print(f'Total income: £{total_income:.2f}\n Total expenses: £{total_expenses:.2f}\n Remaining balance: £{remaining_balance:.2f}')

#Quit the program  
  elif action == '4':
    print("Exiting program, goodbye!")
    break

#Error handling incorrect inputs
  else:
    print("Incorrect input, try again")