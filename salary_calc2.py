# TODO Finish writing the Tax section. Definitely need some functions here


# This is a function to calcuate working days
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
def tax_rate():
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
   
def calc_net_yearly_salary():
    # net_yearly_salary = gross_yearly_salary - (gross_yearly_salary * tax_bracket)
    print("line")

# This is a function to calcuate salary
def salary():
    print(" You earn " + str(gross_yearly_salary) + " before tax")
    print(" You earn " + str(net_yearly_salary) + " after tax")
    # print(" You make " + str(net_yearly_salary / working_days) + " per day")
    # print(" You make " + str(net_yearly_salary / working_days / 8.5) + " per hour")
    # print(" You make " + str(net_yearly_salary / working_days / 8.5 / 60) + " per minute")
    # print(" You make " + str(net_yearly_salary / working_days / 8.5 / 60 / 60) + " per second")

if __name__ == "__main__":
    gross_yearly_salary = int(input("What is your yearly gross salary?"))
    yearly_holidays  = int(input("How many holidays do you get a year?: "))

    working_days()
    tax_rate()
    salary()
    print()
