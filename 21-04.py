dict1 = {1: 'v1', 'k2':'v2', 'k1': 'v2'}
print(dict1['k1'])


dict1['k6'] = 'v5'

print(dict1)



# print(dict1.keys())
# print(dict1.items())


# for i in dict1.keys():
#     print(i, dict1[i])


# for i, j in dict1.items():
#     print(i, j)



list1 = ['orange', 'mango', 'watermelon']
#{'orange': 6, 'mango': 5, 'watermelon': 10}

res = {}
for i in list1:
    res[i] = len(i)

print(res)
    

#List1 and list2 lengths same
list1 = ['orange', 'mango', 'watermelon']
list2 = ['v1', 'v2', 'v3']
res = {}

for i in range(len(list1)):
    res[list1[i]] = list2[i]

print(res)




list1 = [2, 2, 2, -1, 1, 0, -32, 2, -32]
#{2: 4, -1: 1, 1: 1, 0: 1, -32: 2}
res = {} #{2: 2}

for i in list1:
    if i not in res:
        res[i] = 1
    else:
        res[i] = res[i] + 1
        #res[2] = 1 + 1

print(res)






#5
dict1 = {1: 'v1', 'k2':'v2', 'k1': 'v3', 'k4': 'v3'}
res = {}
#{'v1': 1, 'v2': 'k2', 'v3': 'k1'}
#first level - pick any key as value
for i, j in dict1.items():
    res[j] = i

print(res)





#level2 - 
dict1 = {1: 'v1', 2: 'v1' , 'k2':'v2', 'k1': 'v3', 'k4': 'v3'}
#{'v1': [1], 'v2': ['k2'], 'v3': ['k1', 'k4']}

res = {}
for i, j in dict1.items():
    if j not in res:
        res[j] = [i]
    else:
        res[j].append(i)
        #[1].apppend(2)

print(res)



list1 = [2, 2, 2, -1, 1, 0, -32, 2, -32]

max = float('-inf')

for i in list1:
    if i > max:
        max = i
    
print(max)


dict1 = {'k1': 32, 'k2': -3, 'k3': 212, 'k4': 161}

max_value = float('-inf')
max_key = 'No key'
for i,j in dict1.items():

    if j > max_value:
        max_value = j
        max_key = i


print(max_value)
print(max_key)


#Given two dictionaries, merge them into one. 
# If a key exists in both, sum their values.


dict1 = {'k1': 2, 'k2': 5, 'k3': 6}
dict2 = {'k3': 7, 'k5': 55}

#{'k1': 2, 'k2': 5, 'k3': 13, 'k5': 55}

res = {}


for i, j in dict1.items():
    res[i] = j

print(res)


for i,j in dict2.items():
    if i in res:
        res[i] = res[i] + j
    else:
        res[i] = j


print(res)


#Anagrams - 
#STOP, POST, TOPS
#AJAY, JAYA

#ELBOW, BELOW

f_dict1 = {}
f_dict2 = {}

if f_dict1 == f_dict2:
    print("Anagrams")


#STOP - OPST
#POST - OPST
#TOPS - OPST


print(sorted('STOP') == sorted('TOSS'))