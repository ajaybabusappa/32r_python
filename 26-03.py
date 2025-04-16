#Vowels, consonants or neither

# char = input("Enter a single character").lower()


# if len(char) == 1:
#     if char.isalpha():
#         if char in ['a', 'e', 'i', 'o', 'u']: #A, E, I,O U
#             print("Vowels")
#         else:
#             print("Consonants")
#     else:
#         print('Special characters or non alphabets')

# else:
#     print("Invalid Input..len greater than 1")




input = 5
for i in range(1, input + 1):
    for j in range(1, 21):
        print(i,'*', j, '=', i * j)
    print("---------**--------")




#Reverse a integer
#54312
#21345


num1 = 54312
rev_num = 0


while num1 > 0:
    rem = num1 % 10 #2 #1 #3 #4 #5
    print(rem)
    rev_num = rev_num * 10 + rem #2 #21 #213 #2134 #21345
    num1 = num1 // 10 #5431 #543 #54 #5 #0

print(rev_num)


# 532 
# #2, 53
# #3, 5
# #5, 0
