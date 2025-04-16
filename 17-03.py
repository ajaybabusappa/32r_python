#Logical operators - and, or, not

print(True and True)
print(True or False)
print(False or False)
print(False and True)
print(False and False)

print(not (True and False))



print(False and (True and (True and (False and True))))

# print(False or (False or (True or (False or True))))
#Truthy and Falsy values

print(2 and 3)
print(0 and 2)
print('' and 'str')
print([1, 2, 3] and [1])


print(bool(2))
#Truthy values - 2, 3, 'str', [1]
#Falsy values - 0, '', []
# print(2 or 3)

print(2 or 3)
print('' or 5)
print(None or 10)



#Bitwise operators - &, |, ^, >>, <<, ~

num1 = 17
print(bin(num1)) 


num1 = 0b111
print(int(num1))



print (5 & 8)
#5 - 0101
#8 - 1000

print(11 & 14)
#11 - 1011
#14 - 1110

print(11 | 14)

#1011
#1110
#1111


#xor
print(11 ^ 14)

#1011
#1110
#0101

#Left shift and right shift
#<<, >> right shift

print (5 << 3)
print(11 << 1)
print(13 << 1)
# print(5 >> 1)



#5  - 0101

#1 * 1 + 0 * 2 + 1 * 4 + 0 * 8

#01010

#0 * 1 + 1 * 2 + 0 * 4 + 1 * 8 + 0 * 16

# 2 * (5)


