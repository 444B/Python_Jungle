"""
This script is meant to take in yearly holidays and gross salary and calculate 
the net yearly salary, stats about holidays and income and other things.
Run the script bug it is currently in debug mode as I fugure out tax brackets

The script does run as is but it is not finished. Problematic sections in debug mode
have been commented out
I have included a comment on each section mentioning if it currently works or not
"""


def working_days(holidays):
    """ calculates when to take holidays """
    days_of_work = (365 - (58*2) - int(holidays))
    print(f"""
    Working Days Section
    ===========================
    You work {str(days_of_work)} days a year,
    You have about {str(round(holidays/12, 2))} holidays every month,
    For every {str(days_of_work/holidays)} days worked, you earn a day off,
    This is earned every {str((days_of_work/holidays)/5)} weeks,
    You should take a 5 day holiday every {str(round(holidays/12, 2))} weeks!

    """)
    return days_of_work, holidays


# This is a function to calcuate tax brackets
# Works but doesnt seem to export the values to global variables

# by adding a docstring with """ TEXT """, when you put your mouse over the function,
# It shows that text, So it helps people understand what the function does
# Now this function takes in a gross salary and returns the tax bracket %
def tax_bracket(gross_salary):
    """calculates tax bracket"""
    if gross_salary <= 77400:
        return 0.10
    elif gross_salary <= 110880:
        return 0.14
    elif gross_salary <= 178080:
        return 0.20
    elif gross_salary <= 247440:
        return 0.31
    elif gross_salary <= 514920:
        return 0.35
    elif gross_salary <= 663240:
        return 0.47
    elif gross_salary > 663241:
        return 0.50
    else:
        print("Tax can not be calculated, please review numbers provided")

    print("You are taxed at " + str(tax_bracket * 100) + "%")
    # calc_net_yearly_salary()
    return tax_bracket


# ALTERNATE IDEA for tax bracket:
brackets = {"0.10": 77400,
            "0.14": 110880,
            "0.20": 178080,
            "0.31": 247440,
            "0.35": 514920,
            "0.47": 663240}


def tax_bracket2(bracket, gross_salary_amount):
    """calucaltes tax brackets"""
    for key, value in bracket.items():
        if gross_salary_amount <= value:
            return key

        if gross_salary_amount > 663241:
            return 0.50


def calc_net_yearly_salary(bracket, gross_salary):
    """calculats yearly net salary"""
    # add full logic for how tax brackets actually work (i.e each step is taxed at its own rate)
    tax_percent = tax_bracket2(bracket, gross_salary)
    net_salary = gross_salary - (gross_salary * tax_percent)
    return net_salary


def salary(gross_salary):
    """ calculates pre tax earnings """
    # This is a function to calcuate salary
    # Works but need to fix the importing of net_yearly_salary which,
    # is depending on calc_net_yearly_salary()
    print(f" You earn {str(gross_salary)} before tax")
    # print(" You earn " + str(net_yearly_salary) + " after tax")
    # print(" You make " + str(net_yearly_salary / working_days) + " per day")
    # print(" You make " + str(net_yearly_salary / working_days / 8.5) + " per hour")
    # print(" You make " + str(net_yearly_salary / working_days / 8.5 / 60) + " per minute")
    # print(" You make " + str(net_yearly_salary / working_days / 8.5 / 60 / 60) + " per second")


if __name__ == "__main__":
    gross_yearly_salary = int(input("What is your yearly gross salary?"))
    yearly_holidays = int(input("How many holidays do you get a year?: "))

    tax_bracket2(brackets, gross_yearly_salary)
    working_days(yearly_holidays)
    tax_bracket(gross_yearly_salary)
    salary(gross_yearly_salary)
    calc_net_yearly_salary(brackets, gross_yearly_salary)
