# for i in range(0, 14):
#     if i % 7 == 0:
#         continue
#     print(i)



for cmp in range(1, 11):
    for emp_id in range(1, 31):
        if cmp ** 5 < 135 or emp_id < 15:
            break
        print(cmp, emp_id)


#Pass
# i = 10

# if i % 2 == 0:
#     pass
# else:
#     print('dsfa')


# def check_sum():
#     pass



age = 18
print('eligible to vote') if age > 18 else print("Not eligible")


num1 , num2 , num3 = 5, 6, 7

if num1 > num2 and num1 > num3:
    print(num1, 'Is the greteast number')
elif num2 > num3:
    print(num2)
else:
    print(num3)



year = 1796

if year % 400 == 0:
    print("Leap year")
elif year % 100 != 0 and year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap")



if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
    print("Leap year")
else:
    print("Not a leap")