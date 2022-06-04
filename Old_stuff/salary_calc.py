# TODO Write comments
# TODO Rewrite the code into functions
# TODO write init, name, main thingy
# TODO Finish writing the Tax section. Definitely need some functions here


# ------------------------------------------
print("\n")
gross_yearly_salary = int(input("What is your yearly gross salary?"))
yearly_holidays = months = int(input("How many holidays do you get a year?: "))

print("\n")

####################################################
# Working Days Section
print("Working Days Section")
working_days = (365 - (58*2) - int(yearly_holidays))
print("You work " + str(working_days) + " days a year")
print("You have about " + str(round(yearly_holidays/12, 2) ) + " holidays every month")
print("For every " + str(working_days/yearly_holidays) + " days worked, you earn a day off")
print("This is earned every " +str((working_days/yearly_holidays)/5) + " weeks")
# print("You should take a 5 day holiday every " + str(3 / (round(yearly_holidays/12), 2)) + " weeks")
print("\n")

####################################################
# Salary Section
# I should absolutely write a function to work this out
# But I want to work on the logic first and use this as a trial
print("Salary Section")
# https://www.cpa-dray.com/en/blog/income-tax-rates-in-israel/
if gross_yearly_salary <=  77400:
    taxed_income = (gross_yearly_salary/10)
    net_yearly_salary = gross_yearly_salary - taxed_income
    print("You are in the 10% Tax bracket and are paying "+ str(taxed_income) +" in tax")
    
elif gross_yearly_salary <=  110880:
    taxed_income = gross_yearly_salary - 7740
    net_yearly_salary = gross_yearly_salary - taxed_income
    print("You are in the 14% Tax bracket and are paying "+ str(taxed_income) +" in tax")

elif gross_yearly_salary <=  178080:
    taxed_income = (gross_yearly_salary/10)
    net_yearly_salary = gross_yearly_salary - taxed_income
    print("You are in the 20% Tax bracket and are paying "+ str(taxed_income) +" in tax")

elif gross_yearly_salary <=  247440:
    taxed_income = (gross_yearly_salary/10)
    net_yearly_salary = gross_yearly_salary - taxed_income
    print("You are in the 31% Tax bracket and are paying "+ str(taxed_income) +" in tax")

elif gross_yearly_salary <=  514920:
    taxed_income = (gross_yearly_salary/10)
    net_yearly_salary = gross_yearly_salary - taxed_income
    print("You are in the 35% Tax bracket and are paying "+ str(taxed_income) +" in tax")

elif gross_yearly_salary <=  663240:
    taxed_income = (gross_yearly_salary/10)
    net_yearly_salary = gross_yearly_salary - taxed_income
    print("You are in the 47% Tax bracket and are paying "+ str(taxed_income) +" in tax")

elif gross_yearly_salary > 663241:
    taxed_income = (gross_yearly_salary/10)
    net_yearly_salary = gross_yearly_salary - taxed_income
    print("You are in the 50% Tax bracket and are paying "+ str(taxed_income) +" in tax")

else:
    print("Incorrect value")

print(" You earn " + str(gross_yearly_salary) + " before tax")
print(" You earn " + str(net_yearly_salary) + " after tax")
print(" You make " + str(net_yearly_salary / working_days) + " per day")
print(" You make " + str(net_yearly_salary / working_days / 8.5) + " per hour")
print(" You make " + str(net_yearly_salary / working_days / 8.5 / 60) + " per minute")
print(" You make " + str(net_yearly_salary / working_days / 8.5 / 60 / 60) + " per second")


####################################################
# Optimal Holidays Section

