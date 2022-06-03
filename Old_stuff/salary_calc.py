# TODO Write comments
# TODO Rewrite the code into functions
# TODO write init, name, main thingy
# TODO Finish writing the Tax section. Definitely need some functions here


# ------------------------------------------
print("\n")
gross_yearly_salary = int(input("What is your yearly gross salary?"))
yearly_holidays = months = int(input("How many holidays do you get a year?: "))

print("\n")
print("Working Days Section")
working_days = (365 - (58*2) - int(yearly_holidays))
print("You work " + str(working_days) + " days a year")
print("You have about " + str(round(yearly_holidays/12, 2) ) + " holidays every month")
print("For every " + str(working_days/yearly_holidays) + " days worked, you earn a day off")
print("This is earned every " +str((working_days/yearly_holidays)/5) + " weeks")

print("\n")
print("Salary Section")
# https://www.cpa-dray.com/en/blog/income-tax-rates-in-israel/
if gross_yearly_salary <=  77400:
    net_yearly_salary = gross_yearly_salary - (gross_yearly_salary/10)
    print("You are in the 10% Tax bracket and are paying "+ str(gross_yearly_salary/10) +" in tax")
    
elif gross_yearly_salary <=  110880:
    net_yearly_salary = gross_yearly_salary - 7740 - (gross_yearly_salary/14)
    print("You are in the 14% Tax bracket and are paying "+ str(gross_yearly_salary/10) +" in tax")

elif gross_yearly_salary <=  178080:
    net_yearly_salary = gross_yearly_salary - (gross_yearly_salary/10)
    print("You are in the 20% Tax bracket and are paying "+ str(gross_yearly_salary/10) +" in tax")

elif gross_yearly_salary <=  247440:
    net_yearly_salary = gross_yearly_salary - (gross_yearly_salary/10)
    print("You are in the 31% Tax bracket and are paying "+ str(gross_yearly_salary/10) +" in tax")

elif gross_yearly_salary <=  514920:
    net_yearly_salary = gross_yearly_salary - (gross_yearly_salary/10)
    print("You are in the 35% Tax bracket and are paying "+ str(gross_yearly_salary/10) +" in tax")

elif gross_yearly_salary <=  663240:
    net_yearly_salary = gross_yearly_salary - (gross_yearly_salary/10)
    print("You are in the 47% Tax bracket and are paying "+ str(gross_yearly_salary/10) +" in tax")

elif gross_yearly_salary > 663241:
    net_yearly_salary = gross_yearly_salary - (gross_yearly_salary/10)
    print("You are in the 50% Tax bracket and are paying "+ str(gross_yearly_salary/10) +" in tax")

else:
    print("Incorrect value")

print(" You earn " + str(gross_yearly_salary) + " before tax")
print(" You earn " + str(net_yearly_salary) + " after tax")
print(" You make " + str(net_yearly_salary / working_days) + " per day")
print(" You make " + str(net_yearly_salary / working_days / 9) + " per hour")
print(" You make " + str(net_yearly_salary / working_days / 9 / 60) + " per minute")
print(" You make " + str(net_yearly_salary / working_days / 9 / 60 / 60) + " per second")
