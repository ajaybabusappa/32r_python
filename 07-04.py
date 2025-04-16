# list1 = [2, -5, 77, 82, -30]

# sum = 0
# for i in list1:
#     sum += i

# print(sum)


# sum = 0
# for i in range(0, len(list1)):
#     sum += list1[i]

# print(sum)


# for i in list1:
#     if i % 2 == 0:
#         print(i)



# for i in range(0, len(list1)):
#     if i % 2 == 0:
#         print(list1[i])


# #1 2 -1 -3 5 10

# list1 = [-2, -5, -77, -82, -30]
# max_ele = list1[0] #2 #77 #82
# min_ele = list1[0]

# max_ele = float('-inf')
# min_ele = float('inf')

# for i in list1: #2 #-5 #77 #82
#     if i > max_ele:
#         max_ele = i
#     if i < min_ele:
#         min_ele = i

# print(max_ele)


#
list1 = [153, 370, 9474, 154]


def check_armstrong(input_num):
    num1 = input_num
    temp = num1
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum += digit ** len(str(num1))
        temp = temp // 10

    if sum == num1:
        print(num1, "Armstrong number")
    else:
        print(num1, "Armweak number")


for i in list1:
    check_armstrong(i)




#
list1 = [1, 2, 3, 82, -30, 44]  #10 #1000
#[44, -30, 82, 3, 2, 1]
#Method 1

new_list = [] #10 #1000
for i in list1:
    print(i)
    new_list.insert(0 , i)

list1 = new_list
print(list1)

#O(n) - Space complexity


# new_list.append(5)
# new_list.insert(0, 3)



# for i in list1:
#     print(i)
#     new_list.append(i)

# list1 = new_list
# print(list1)




list1 = [1, 2, 3, 82, -30, 44]
#[1, 2, 3, 44, -30, 82]

low = 0
high = len(list1) - 1 #5

while high > low:
    list1[low], list1[high] = list1[high], list1[low]
    low += 1
    high -= 1

print(list1)




list1 = [1, 2, 3, 82, -30, 44]
find = 31


flag = False
for i in range(len(list1)):
    if list1[i] == find:
        flag = True
        print(i)
        break


if flag == False:
    print("Not found")


list1 = [1, 2, 3, 82, -30, 44]
find = -30

def linear_search(input_list, find_elem):
    for i in range(len(input_list)):
        if input_list[i] == find_elem:
            return i
        
    return 'Not found'


print(linear_search(list1, find))

#O(1) - S.C
#O(n) - T.C



#Binary search - Sorted lists 




list2 = [1, 5, 10, 22, 72, 88, 91, 97, 110]
search_elem1 = 100

def bin_search(list1, search_elem):
    low = 0
    high = len(list1) - 1

    while low <= high:
        mid = (low + high) // 2
        if list1[mid] == search_elem:
            return mid
        elif list1[mid] > search_elem:
            high = mid - 1
        else:
            low = mid + 1

    return 'Not found'

print(bin_search(list2, search_elem1))

#T.C - O(logn)
#S.C - O(1)





