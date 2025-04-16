# while True:
#     num1 = int(input("Enter a non negative number"))
#     if num1 < 0:
#         print("You didn't follow the rules...Nen bhongu muthi pettukunna")
#         break
    
    
    
# num1 = int(input("Enter a non -ve number"))
# while num1 >= 0:
#     print(num1)
#     num1 = int(input("Enter a non -ve number"))



# f(n) = f(n-1) + f(n-2) # if n = 0 f(n) = 0 and if n = 1 f(1) = 1


# num1, num2 = 0, 1

# n = 20

# for i in range(0, 20):
#     print(num1)
#     num3 = num1 + num2
#     num1 = num2
#     num2 = num3
#     #num1, num2 = num2, num1 + num2
    
    

db_username = 'Shinchan'
db_password = 'snanam chesava?'

rem_attempts = 3

while rem_attempts > 0:
    input_username = input("Enter username")
    input_password = input("Enter password")

    if input_username == db_username and input_password == db_password:
        print("Login succesful")
        break
    else:
        rem_attempts -= 1
        if rem_attempts == 0:
            print("Repu kaludham")
        else:
            print('login failed', 'you still have' ,rem_attempts)
    