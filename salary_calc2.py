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
    days_of_work = (249 - int(holidays))
    print(f"""
    Working Days Section
    ===========================
    You work {str(days_of_work)} days a year,
    You have about {str(round(holidays/12, 2))} holidays every month,
    For every {str(days_of_work/holidays)} days worked, you earn a day off,
    This is earned every {str((days_of_work/holidays)/5)} weeks,
    You should take a 5 day holiday every {str(round(holidays/12, 2))} weeks!

    """)
    return days_of_work


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


# ALTERNATE IDEA for tax bracket:
brackets = {
    0.10: 77400,
    0.14: 110880,
    0.20: 178080,
    0.31: 247440,
    0.35: 514920,
    0.47: 663240
}


def tax_bracket2(bracket, gross_salary_amount):
    """calucaltes tax brackets"""
    for key, value in bracket.items():
        if gross_salary_amount > 663241:
            return 0.50

        if gross_salary_amount <= value:
            return key


def calc_net_yearly_salary(gross_salary):
    """calculats yearly net salary"""
    # add full logic for how tax brackets actually work (i.e each step is taxed at its own rate)
    tax_percent = tax_bracket(gross_salary)
    net_salary = gross_salary - (gross_salary * tax_percent)
    return net_salary


def salary(gross_salary, holidays):
    """ calculates salary earnings """
    net_salary = calc_net_yearly_salary(gross_salary)
    work_days = working_days(holidays)

    print(f"""
    Your Earnings
    ===========================
    You earn {str(gross_salary)} before tax,
    You earn {str(net_salary)} after tax"
    Which is, {str(net_salary / work_days)} per day,
    {str(round(net_salary / work_days / 8.5))} per hour,
    {str(round(net_salary / work_days / 8.5 / 60, 3))} per minute,
    {str(round(net_salary / work_days / 8.5 / 60 / 60, 2))} per second

    """)


def user_input_checker(input_question):
    """Gets and checks user inputs"""
    while True:
        try:
            user_input = int(input(input_question).strip())
        except ValueError:
            print("Sorry, that is not a valid input (positive numbers only)")
            continue
        # Makes it so you don't get a ZeroDivisionError,
        # if you put in 0 for yearly_holidays(in the other functions)
        if user_input >= 1:
            return user_input
        else:
            print("Sorry, input must be greater than 1")
            continue


def main():
    """main function"""
    gross_yearly_salary = user_input_checker(
        "What is your yearly gross salary?: ")

    yearly_holidays = user_input_checker(
        "How many holidays do you get a year?: ")

    salary(gross_yearly_salary, yearly_holidays)


if __name__ == "__main__":
    main()
