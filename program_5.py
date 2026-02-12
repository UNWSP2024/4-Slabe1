# Program #5: Bank Balance
# Write a program that asks the user to enter the amount that he or she has budgeted for a month.
# A loop should then prompt the user to enter each of his or her expenses for the 
# month and keep a running total. (Enter 0 to exit the loop)  
# When the loop finishes, the program should display the amount that the 
# user is over or under budget.

def main():
    budget = 0.0
    difference = 0.0
    spent = 0.0         #initialize for while loop
    total = 0.0

    input_another_expense = True
    budget = float(input("What is your budget for this month?  "))
    
    while input_another_expense:

        spent = float(input("Input an expense: "))

        if spent < 0:
            spent = float(input("ERROR  Please input a positive number: "))

        if spent == 0:
            break
        
        total += spent
        print(f"Total spending: {total}")
        

    difference = budget - total
    if difference < 0:
        print(f"You are ${difference} over budget")
    else:
        print(f"You have ${difference} remaining in your budget")



if __name__ == '__main__':
    main()