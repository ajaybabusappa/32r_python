# str1 = 'you are scree sharing'


# #Method 1
# new_str = ''

# for i in str1:
#     new_str = i + new_str  #oy

# print(new_str)
# # str1 = new_str



# #Method 2
# print(str1[::-1])
# str1 = str1[::-1]


# #Method 3 - Recursion


# #
# str1 = 'a+((b-c)+d)'

# new_str = ''
# for i in str1:
#     if i not in ['(', ')', '[', ']', '{']:
#         new_str =  new_str + i

# print(new_str)


# count = 0
# for i in str1:
#     if i == ' ':
#         count += 1

# print(count)


# str1 = 'take u forward is awesome'
# #iu

# vowel_dict = {}
# for i in str1:
#     if i in ['a', 'e', 'i', 'o', 'u']:
#         if i not in vowel_dict:
#             vowel_dict[i] = 1
#         else:
#             vowel_dict[i] = vowel_dict[i] + 1


# for i,j in vowel_dict.items():
#     if j == 1:
#         print(i)

    


# str1 = 'google docs are better then word docs'
# #Level 1 - Any one
# #Level 2 - Both 

# list1 = str1.split()

# max_string = ''
# for i in list1:
#     if len(i) > len(max_string):
#         max_string = i

# print(max_string)
    


# #Level 2
# str1 = 'google docs are better then word docs'
# #Level 1 - Any one
# #Level 2 - Both 

# list1 = str1.split()



# max_len = 0

# for i in list1:
#     if len(i) > max_len:
#         max_len = len(i)

# print(max_len)


# for i in list1:
#     if len(i) == max_len:
#         print(i)



# # Return the longest palindromic substring in a string
# #      Inp:”abccbc” there are a b c cc bccb  cbc   
# #        Out : bccb


# #abccbc
# #a
# #ab
# #abc
# #abcc
# #abccb
# #abccbc
# #b
# #bc
# #bcc
# #bccb
# #bccbc


# #Step2 - Find palindrome among those

# def check_palindrome(input_str):
#     return input_str == input_str[::-1]

# str1 = 'abccbc'
# #Step 1 - Find the substrings


# max_string = ''
# for i in range(len(str1)): #1
#     for j in range(i+1, len(str1) + 1): # 2 to 6
#         if check_palindrome(str1[i:j]):
#             if len(str1[i:j]) > len(max_string):
#                 max_string = str1[i:j]

# print(max_string)
            


# str1 = 'takeuforward'
# str2 = 'forward'


# for i in range(len(str1)):
#     # print(str1[i: i + 7])
#     if str1[i: i + len(str2)] == str2:
#         print(i)
#         break


#Step 3 - Find longest among those palindromes




#OOPS - Object oriented programming


#Calculator - 

#Class : 
#Object or instance

#CASIO 
class Calculator: #Blueprint or definition

    company_name = 'CASIO'
    def __init__(self, id1, color1, manf_date1):
        self.id = id1
        self.color = color1
        self.manf_date = manf_date1
        print("This is a constructor")

    
    def print_id(self):
        print(Calculator.company_name)
        print(self.id)


    def add(self):
        print("This is an add function") 
    
    def mul(self):
        print("This is a function for multiplication")


    @classmethod
    def change_company_name(cls, new_name):
        cls.company_name = new_name
        print("Company name changed")

    @staticmethod
    def print_company_desc():
        print("This is a good company")


calc1 = Calculator(1, 'black', '01Feb')
calc2 = Calculator(2, 'White', '01Feb')

calc1.expiry = '28Feb'

print(vars(calc1))
print(vars(calc2))

print(calc1.id)
print(calc2.manf_date)

calc1.add()
calc2.add()

# calc1.id = 12
# calc1.color = 'black'
# calc1.manf_date = '01Feb'
# calc1.id = 14


# calc2.id = 12
# calc2.color = 'black'
# calc2.manf_date = '01Feb'



#Constructor - Is also a method




#Types of variables - 2 types - 1. Instance variables 2. Class/static variables

# calc1 = Calculator(1, 'black', '01Feb')
# calc2 = Calculator(2, 'White', '01Feb')

# print(calc1.id)
# print(calc2.color)
# print(calc1.company_name)
# print(Calculator.company_name)
# print(Calculator.id)
# print(Calculator.manf_date)



#Types of methods - 3 methods - Instance methods, class methods, static methods

#Instance methods - Any methods which has atleast one instance variable is called instance method

calc1.print_id()
calc2.print_id()
# Calculator.print_id()
Calculator.change_company_name('NEW_CASIO')
calc1.change_company_name('NEW_CASIO2')
print(calc1.company_name)


#class methods - only class/static variables


