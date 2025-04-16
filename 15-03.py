# #range

# rng1 = range(0, 11)
# print(list(rng1))

# rng2 = range(11, 0, -2)
# print(list(rng2))


# #-2, 25 - I want all even numbers
# rng3 = range(-1, 25, 2)
# print(list(rng3))

# #Set - collection of hetrogenous, unique elements, unordered

# s1 = {1, 2, 5, 6, 7, 9, 1.5, "String example", 'String2', 'String 3'}
# print(type(s1))
# print(s1)

# list1 = [1, 5, 10, 11, 11]


# #Dictionary - key and value pairs
# # roll numbers can not be duplicate - (or) roll numbers are unique
# #values or names 


# dict1 = {1: 'Mahesh', 2 : 'Mahesh', '21' : 'Krish', 1: 'Suresh', 1: 'Rakesh'}
# print(dict1)
# # print(dict1['Mahesh'])
# dict1['21'] = 'Kamsa mama'
# print(dict1)


# # db_values = {'db_name': 'localhost/3000', 'db_password': 'Secret', 'timeout': 30}
# # ['localhost/3000', 'Secret', 30]


# #Datatype - None - empty

# #None

# dt = None
# print(type(dt))

# dt = 5
# print(dt)

# #Why strings are python are immutable


# str1 = 'hi'
# str2 = 'hi'
# print(id(str1))
# print(id(str2))

# str2 = 'hi there'
# print(str2)


# num1 = 5
# print(id(num1))
# num1 += 1
# print(id(num1))



#type conversion
num1 = 4.5
print(int(num1))
num1 = int(num1)
print(num1)

num1 = 4.5
num1 = int(num1) #4
num1 = float(num1) #4.0
print(num1)


str1 = 'string example'
print(list(str1))
print(str1)


cmp1 = 2 + 1j
# print(int(cmp1))

str1 = '145.5'
print(float(str1))
print(int(str1))



#         int float  cmp boolean list
# int 

# float

# cmp

# boolean

# list 