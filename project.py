
num1 = int(input("Enter a number: "))
sign = input("Enter a Sign: ")
num2 = int(input("Enter another number: "))
if sign == '+':
    print("Summation Result: ", num1 + num2)
elif sign == '-':
    print("Subtraction Result: ", num1 - num2)
elif sign == '*':
    print("Multification Result: ", num1 * num2)
elif sign == '/':
    print("Division Result: ", num1 / num2)
elif sign == '//':
    print("Floot Division Result: ", num1 // num2)
elif sign == '%':
    print("Modulus Result: ", num1 % num2)
elif sign == '**':
    print("Power Result: ", num1 ** num2)
else:
    print("Invalid Sign.")
