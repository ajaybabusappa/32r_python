#*
#* *
#* * *
#* * * *



#    *
#   * *
#  * * *
# * * * *
#* * * * *

#i == n-1 => spaces = 0 => 0 == n - i - 1 => spaces = n-i-1
#i == n-2 => spaces = 1 => 0 == n-i-2  => spaces - 1 = n - i - 2 => spaces = n-i-1
#i == n-3 => spaces = 2






n = 7
for i in range(n):

    for k in range(n - i -1):
        print(" ", end= '')

    for j in range(n):
        if i == j or i == n - 1 or j == 0:
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()




# Fibonocci
n = 7
num1, num2 = 0, 1
for i in range(n):

    for j in range(n):
        if i >= j:
            print(num1, end=' ')
            num1, num2 = num2, num1 + num2
    print()




#  
# #
# #       1
# #     2 1 2 
#     3 2 1 2 3 
#   4 3 2 1 2 3 4
# 5 4 3 2 1 2 3 4 5


#last_row = 0
#n-2 => 2
#n - 3 => 4


#i == 0 => stars = 1
#i == 1 => stars = 3
#i == 2 => stars = 5
#i == 3 => stars = 7 =>

#2*i + 1

n = 5


for i in range(n):
    track1 = False
    start = i + 1
    for k in range(2*(n-i-1)):
        print(' ', end='')

    for j in range(2 * i + 1):
        print(start, end=' ')
        if start == 1:
            track1 = True
        
        if track1 == False:
            start -= 1
        else:
            start += 1

    print()


print('--------------------')

#Method 2

#3 rd row ; i == 2
i = 2

str1 = ''

for i in range(1, i + 2): #1, 2, 3
    str1 = str1 + str(i) + ' '
    #str1 = '' + '1' + ' ' => str1 = '1 '
    #str1 = '1 ' + '2' + ' ' => str1 = '1 2 3 '

i = 2
for i in range(i, i + 2):
    str1 = str(i) + ' ' + str1


print(str1)





#OOPS 
#Inheritance - 
#Polymorphism - 
#Encapsulation - 
#Abstraction - 


class HumanBeing:
    def __init__(self, name, gender, dob):
        self.__name = name
        self._gender = gender
        self.dob = dob
        print("Human object created")
    

    def introduce(self):
        print(self.__name, self.dob)


    def get_name(self):
        return self.__name
    
    def set_name(self, new_name):
        self.__name = new_name
        print("Name changed")



class Student(HumanBeing):
    pass


hm1 = HumanBeing('Sampurnesh Babu', 'Male', '24Feb')
# print(hm1.name)
# hm1.name = 'Mahesh babu'

# hm1.get_name()
# hm1.set_name()
# print(hm1.__name)
print(hm1._gender)

#Access specifiers - public, private and protected
#private variable - double underscore




#Abstraction - Hiding internal implementaion of methods

#atm vendor
#You cannot create an object for abstract class

from abc import ABC, abstractmethod

class ATM(ABC):

    @abstractmethod
    def check_balance(self):
        pass

    @abstractmethod
    def deposit(self):
        pass

    @abstractmethod
    def withdrawl(self):
        pass

    def info_atm(self):
        print("This is info of atm")




class SBI_ATM (ATM):

    def check_balance(self):
        #SBI
        print("0 rupees")

    def deposit(self):
        print("Money deposited")

    def withdrawl(self):
        print("Money withdrawn")
    




class ICICI_ATM (ATM):

    def check_balance(self):
        #ICICI'S OWN LOGIC
        print("ICICI 0 rupees")

    def deposit(self):
        print("ICIIC Money deposited")

    def withdrawl(self):
        print("ICICI Money withdrawn")

ici_atm = ICICI_ATM()





#Swapping


a = 10
b = 20
a, b = b, a


#Method 2

a, b = 10, 20

temp = b
b = a
a = temp



#Method 3

a, b = 10, 20

a = a + b #30
b = a - b #10
a = a - b #30 - 10 #20