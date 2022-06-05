""" 
This script is meant to take in yearly holidays and gross salary and calculate 
the net yearly salary, stats about holidays and income and other things.
Run the script bug it is currently in debug mode as I fugure out tax brackets

The script does run as is but it is not finished. Problematic sections in debug mode
have been commented out
I have included a comment on each section mentioning if it currently works or not
"""

# This is a function to calculate working days
# Works
def working_days():
    working_days = (365 - (58*2) - int(yearly_holidays))
    print("Working Days Section")
    print("You work " + str(working_days) + " days a year")
    print("You have about " + str(round(yearly_holidays/12, 2) ) + " holidays every month")
    print("For every " + str(working_days/yearly_holidays) + " days worked, you earn a day off")
    print("This is earned every " +str((working_days/yearly_holidays)/5) + " weeks")
    print("You should take a 5 day holiday every " + str(round(yearly_holidays/12, 2)) + " weeks")
    print("\n")
    return working_days, yearly_holidays


# This is a function to calcuate tax brackets
# Works but doesnt seem to export the values to global variables
def tax_bracket():
    if gross_yearly_salary <=  77400:
        tax_bracket = 0.10
    elif gross_yearly_salary <=  110880:
        tax_bracket = 0.14        
    elif gross_yearly_salary <=  178080:
        tax_bracket = 0.20
    elif gross_yearly_salary <=  247440:
        tax_bracket = 0.31
    elif gross_yearly_salary <=  514920:
        tax_bracket = 0.35
    elif gross_yearly_salary <=  663240:
        tax_bracket = 0.47
    elif gross_yearly_salary > 663241:
        tax_bracket = 0.50
    else:
        print("Tax can not be calculated, please review numbers provided")

    print("You are taxed at " + str(tax_bracket * 100) + "%")
    calc_net_yearly_salary()
    return tax_bracket
# This is a function to calcuate net salary after tax deductions
# work in progress
def calc_net_yearly_salary():
    # TODO add logic and find a way to correct export the values since i dont seem to be using "return" correctly
    # TODO add full logic for how tax brackets actually work (i.e each step is taxed at its own rate)
    # net_yearly_salary = gross_yearly_salary - (gross_yearly_salary * tax_bracket)
    # return net_yearly_salary
    print("Work in progress")

# This is a function to calcuate salary
# Works but need to fix the importing of net_yearly_salary which is depending on calc_net_yearly_salary()
def salary():
    print(" You earn " + str(gross_yearly_salary) + " before tax")
    # print(" You earn " + str(net_yearly_salary) + " after tax")
    # print(" You make " + str(net_yearly_salary / working_days) + " per day")
    # print(" You make " + str(net_yearly_salary / working_days / 8.5) + " per hour")
    # print(" You make " + str(net_yearly_salary / working_days / 8.5 / 60) + " per minute")
    # print(" You make " + str(net_yearly_salary / working_days / 8.5 / 60 / 60) + " per second")

if __name__ == "__main__":
    gross_yearly_salary = int(input("What is your yearly gross salary?"))
    yearly_holidays  = int(input("How many holidays do you get a year?: "))

    working_days()
    tax_bracket()
    salary()
    print()
