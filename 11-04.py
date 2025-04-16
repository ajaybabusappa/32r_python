# list1 = [-22, 32, -5, 100, -222]
# #
# list1 = [[1, 2], [-3, 4, 5], [22, 27], [-35]]

# for j in range(len(list1)-1):
#     flag = False
#     for i in range(len(list1)-j-1):
#         if list1[i][0] > list1[i+1][0]:
#             flag = True
#             list1[i], list1[i+1] = list1[i+1], list1[i]
    
#     if flag == False:
#         break

# print(list1)


# #S.C => O(1)
# #T.C => O(nlogn)

# #
# list1 = [[1, 2], [-3, 4, 5], [22, 27], [-35]]
#[[-35], [-3, 4, 5], [1, 2], [22, 27]]





# Find the missing numbers.
# Input: 34571      Outpur : 26 missing
#7 and 1 => 26


#.append() => [1, 7, 5, 4, 3]
#max(list1) => 7
#min(list1) => 1


num1 = 4559 #4559
temp = num1
dig_list = []

while temp > 0:
    digit = temp % 10
    print(digit)
    dig_list.append(digit)
    temp = temp // 10 #3457

print(dig_list)


max_elem, min_elem = max(dig_list), min(dig_list)


for i in range(min_elem, max_elem + 1):
    if i not in dig_list:
       print(i) 


#Find if list1 is subset of list2
arr1=[1,3,4,5,2, 100]
arr2=[2,4,3,1,7,5,15]


def check_subset(list1, list2):

    for i in list1:
        if i not in list2:
            return "Not a subset"
    
    return 'Subset'


print(check_subset(arr1, arr2))



#Method 1
# Find Second Largest element in list. (3rd later)
list1 = [20, 15, 26, 2, 98, 98, 6, 36] #98
list1 = set(list1)
list1 = list(list1)
list1.sort()
print(list1[-2])

#Method 2


max_elem = float('-inf')

for i in list1:
    if i > max_elem:
        max_elem = i

print(max_elem)

#list1 = [20, 15, 26, 2, 98, 98, 6, 36] #first_max = 98
second_max = float('-inf')
for i in list1:
    if i > second_max and i != max_elem:
        second_max = i #20 #26 #36

print(second_max)



list1 = [1, 2, 2, 3, 3, 5, 6, 7, 8, 1, 1, 1, 1]
visited_list = []
set1 = set()

for i in list1:
    if i in visited_list:
        print(i, 'Is dupliacte')
        set1.add(i)
    else:
        visited_list.append(i) #[1, 2, 3]


print(list(set1))
dup = list(set1)
#[2, 3, 1]

for i in list1:
    if i not in dup:
        print(i, 'unique')


#15 April

list1 = [20, 15, 26, 2, 98, 6]

#Method 1
# temp = []
# temp.extend(list1)

# temp.sort()
# print(temp)
# print(list1)

#method 2

# temp = list1
# temp.sort()
# print(temp)
# print(list1)

#sorted() 
#method 3

list1 = [20, 15, 26, 2, 98, 6]


new_list = sorted(list1)
print(list1)
print(new_list)


#method 4 - Deepcopy

import copy
new_list = copy.deepcopy(list1)
new_list.sort()
print(new_list)
print(list1)



output = []
for i in list1:
    # temp_res = new_list.index(i)
    # print(temp_res + 1)
    output.append(new_list.index(i) + 1)

print(output)





#Strictly increasing order

list1 = [568, 89, 112, 88, 571]



def check_inc_order(input_num):
    temp = input_num #568
    prev = 10
    while temp > 0: #
        digit = temp % 10 #8 #6 #5
        print(digit)
        if digit >= prev: 
            return False
        prev = digit #8 #6 #5
        temp = temp // 10 #56 #5 #0
    
    return True

# print(check_inc_order(138))
print('----------------------------')
for i in list1:
    print(check_inc_order(i))


#GCD, LCM and Nearest prime
#LCM - x, y

#7, 5 => 35
#2, 4 => 4
#4, 10 => 20
#4, 8, 12, 16, 20, 24, 28, 32, 40
#10, 20, 30, 40, 50


# m, n => max(m,n) to m*n

#6, 24 => 24
#1, 19 => 1 * 19
#4, 10 => 10 to 40 



m = 10
n = 16

max_num = m if m > n else n

for i in range(max_num, m * n + 1):
    if i % m == 0 and i % n == 0:
        print(i, 'is the LCM')
        break

#GCD => 1 to min(m,n)
#2, 4 => 2
#1, 17 => 1
#2, 3 => 1


#LCM * GCD = m * n 




#Nearest Prime Number

#19 => 23

num1 = 19


while True:
    num1 += 1
    #write a function to check if num is prime
    #if num1 is prime
    #print num1 and break



