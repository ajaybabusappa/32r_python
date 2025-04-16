# num1 = float(input("Enter first number"))
# num2 = float(input("Enter second number"))
# #add, sub, mul, div, +, -, *, /, ADD, Add, aDd, SUB, Sub
# op = input("Enter operator").lower() #ADD, Add, aDd => add

# #1, 2, ADD
# print('add' == 'ADD')

# if op in ['add', '+', 'a', 'ad']:
# # if op == 'add' or op == '+' or op == 'a' or op = 'ad':
#     print(num1 + num2)
# # elif op == '+':
# #     print(num1 + num2)
# elif op == 'sub':
#     print(num1 - num2)
# elif op == 'mul':
#     print(num1 * num2)
# elif op == 'div':
#     if num2 != 0:
#         print(num1 / num2)
#     else:
#         print("Division by zero is not possible")
# else:
#     print("Invalid input")




# num1 = 10
# if num1 % 2 == 0:
#     print("Even")
# else:
#     print("Odd")



num1 = 15

#3, 5 => 15, 30, 45


if num1 % 15 == 0:
    print("Fizz Buzz")
elif num1 % 5 == 0:
    print("Buzz")
elif num1 % 3 == 0:
    print("Fizz")
else:
    print("Invalid")



#1700, 1800 => 400 divisibility
#1990 => 4