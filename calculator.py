num1 = float(input("Enter a number: "))

sign = input("provide an action +/-/*//")

num2 = float(input("Enter another number: "))

if type(num1) == float and type(num2) == float: 
    if sign == "+":
        print(num1 + num2)
    elif sign == "-":
        print(num1 - num2)
    elif sign == "*":
        print(num1 * num2)
    elif sign == "/":
        print(num1 / num2)
    else:
        print("Invalid input, ERROR 16")
else:
    print("Invalid input, check your number types")