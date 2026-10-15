print("Welcome to the Personal Finance Tracker!")
print("This program will help you track your income, expenses, and savings goals.")
print("Please enter your financial information below.")
total_income = float(input("How much have you made this month after taxes? "))
total_expenses = float(input("How much have you spent this month? "))
Remaining_balance = total_income - total_expenses
print("Your remaining balance is: $" + str(Remaining_balance))
saving_goal = float(input("What is your savings goal for this month? "))
if Remaining_balance >= saving_goal:
    print("Congratulations! You have met your savings goal.")     
else:
    print("You have not met your savings goal. You need to save $" + str(saving_goal - Remaining_balance) + " more to reach your goal.")
Investment = input("Would you like to invest your remaining balance? (yes/no) ")
if Investment.lower() == "yes":
    print("Great! You can consider investing in stocks, bonds, or mutual funds.")
Choice = input("Would you like to create a budget for next month? (yes/no) ")
if Choice.lower() == "yes":
    print("Let's create a budget for next month.")
print("Please enter your expected income for next month.")
expected_income = float(input("Expected income: "))
total_income_next_month = float(input("Expected income: "))
print("Please enter your expected expenses for next month.")
expected_expenses = float(input("Expected expenses: "))
total_expenses_next_month = float(input("Expected expenses: "))
total_remaining_balance_next_month = total_income_next_month - total_expenses_next_month
print("Your expected remaining balance for next month is: $" + str(total_remaining_balance_next_month))
Target_saving_goal_next_month = float(input("What is your savings goal for next month? "))
if total_remaining_balance_next_month >= Target_saving_goal_next_month:
    print("Congratulations! You are on track to meet your savings goal for next month.")
else:
    print("You are not on track to meet your savings goal for next month. You need to save $" + str(Target_saving_goal_next_month - total_remaining_balance_next_month) + " more to reach your goal.")

    if total_remaining_balance_next_month < 0:
        print("Warning: You are spending more than you are earning. Please consider reducing your expenses or increasing your income.")
print("Thank you for using the Personal Finance Tracker! Remember to review your finances regularly and make adjustments as needed.")