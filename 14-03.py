print(5 + 5)
str1 = "checing strings"
print(str1[5: 5])


#Datatypes -
#Numerics - Int, float, boolean and complex

cmp1 = 2 + 5j
cmp2 = 3 - 1j

print(cmp1 ** cmp2)
#works - +, -, *, /, **
#Does not work - //, %

db_pin = 7203
user_input_pin = 7204

print(db_pin == user_input_pin)
#True
#False

#Sequences - string
# List -
list1 = [2, 5.4, True, 'False', 2 + 3j, [6, 7, 9]]
print(list1[0])
list1[0] = 10
print(len(list1))
print(list1[5][1])
print(list1[5][1])

list1.append(55) #extend, insert
list1.insert(0, 32)
print(list1)

#Tuple - Immutability, comparitevly faster than list
tup1 = (2, 3, 'True', True)
print(tup1[2: 4])
#tup1[0] = 2.5

tup1 = (2, 3)
print(tup1)


# str1 = 'Happy New Year'
# str1[4] = 'v'
# str1[2: 4] = 'ab'


#range

r1 = range(1, 10)
print(list(r1))

print(list(range(-5, 22)))
print(list(range(35, 22, -2)))


#list - 6 elements - 0 to 5
range(0, 6)