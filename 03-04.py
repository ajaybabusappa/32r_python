# #Scope - Accesibility of a variable or an entity is called scope
# #Scopes - Local and global scope

# # print(num1)

# # num1 = 10


# # print(num1)


# # def check():
# #     print(num1)

# # if 5>2:
# #     print(num1)



# # #local variable
# # def check_local():
# #     num2 = 25
# #     print(num2)


# # check_local()
# # print(num2)



# count = 2
# def prime_num():
#     input_num = 10
#     count = 0
#     if count == 2:
#         print("Good Morning")
#     for i in range(1, 10):
#         if input_num % i == 0:
#             return False
#     return True

# prime_num()


# if count == 2:
#     print("Prime")
# else:
#     print("Not prime")



# num1 = 10

# def check():
#     globals()['num1'] = 16
#     num1 = 5
#     print(num1 + 1)

# check()

# print(num1)




# #lambda functions - they have return statements
# #Anonymous one line functions



# example_lambda = lambda x : x * 2
# print(example_lambda(5))
# print(example_lambda(10))
# print(example_lambda(13))


# # example_lambda = lambda x, y: x + y
# # print(example_lambda(2, 7))
# # example_lambda = 10
# # print(example_lambda(2, 7))



# #Higher order functions - 
# #map
# #filter
# #reduce


# def dbl(y):
#     return y * 2

# def trp(y):
#     return y * 3

# print(list(map(lambda x: x * 4 , [10, 20, 45, 64, 75])))

# print(list(map(lambda x: x * 2, [11, 23, 50, 66, -7])))



# #Filter


# print(list(filter(lambda x: x > 0 and x < 22, [11, 23, 50, 66, -7])))



# #Reduce 

# from functools import reduce

# print(reduce(lambda x, y: x - y, [11, 23, 50, 66, -7]))



#Decorators - These are also functions

#Check cartridge and a4 sheets
#System is going to sleep mode

def example_decorator(func):
    def wrapper():
        
        print("Check cartridge and a4 sheets")
        print("System is going to sleep mode")
        func()
    return wrapper


@example_decorator
def printer():
    print("Hi, Printing in progress")
    print('Completed, Bye')


printer()

