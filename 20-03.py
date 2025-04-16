# # #Operators - 
# # #Bitwise operators - &, |, ^, >>, <<, ~
# # #left shift

# # print(5 << 2)
# # print(23 << 1)

# # print(-12 << 1)


# # #Right shift

# # print(5 >> 1)
# # print(10 >> 1)

# # print(25 >> 2)

# # #5 => 0101 => 0010 #2 # 0100
# # #10 => 1010 =>  0101 => 5


# # #0101 => 
# # #1010




# # #~
# # print(~12)
# # print(~25)
# # print(~-13)
# # print(~33)


# #Control statements - control's flow of execution 
# #different types - conditional statements, loops, jump statements - break, continue, pass



# print("")
# print('I cannot vote')



#Conditional statements - if else, elif

age = 18

if age >= 18:
   dob = '2025'
   print('I can vote')
   print('Hi')
   print('Hi Hi')
else:
 print("I cannot vote")
print("Check")


num1 = 6

# if num1 % 2 == 0:
#   print("Even")

# if num1 % 2 != 0:
#   print("Odd")


if num1 % 2 == 0:
  print("Even")

else:
  print("Odd")




num1 = 0
if num1 > 0:
  print("Positive")
else:
  if num1 == 0:
    print("Zero")
  else:
    if num1 == -1:
      print(-1)
    else:
        print("Negative")

#elif

num1 = -3
if num1 > 0:
  print("Positive")
elif num1 == 0:
  print("Zero")
elif num1 == -1:
  print("-1")
elif num1 < 0:
  print("Negative")
else:
  print("Something")




