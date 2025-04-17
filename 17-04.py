#Multidimensional lists or Matrix
#m * n order matrix

mat1 = [
    [2, 5, 3, 4], 
    [4, 7, 1, 5], 
    [3, 0, 5, 8],
    [5, 1, 9, 2]
]

# sum = 0
# for i in mat1:
#     for j in i:
#         sum += j

# print(sum)

# print(mat1[1][2])


# sum = 0
# for i in range(len(mat1)):
#     for j in range(len(mat1[i])):
#         if i == j or i + j == len(mat1) - 1:
#             sum += mat1[i][j]
#             print(mat1[i][j], end=' ')
#         else:
#             print(' ', end=' ')
#     print()
# print(sum)




#0, 3 => 3
#1, 2 => 3
#2, 1 => 3
#3, 0 


#0, 2 => 2
#1, 1 => 2
#2, 0 => 2

# i + j == n - 1
#n is len of square matrix


mat1 = [
    [2, 5, 3, 4], 
    [4, 7, 1, 5], 
    [3, 0, 5, 8],
    [5, 1, 9, 2]
]

mat2 = [
    [-2, 5, 3, 4], 
    [4, 7, 1, 5], 
    [3, 0, 5, 8],
    [5, 1, 9, 2]
]


mat3 = []

for i in range(len(mat1)):
    mat3.append([])
    for j in range(len(mat1[i])):
        #print(mat1[i][j] + mat2[i][j], end=' ')
        mat3[-1].append(mat1[i][j] + mat2[i][j])
    print()

print(mat3)



#Transpose of a matrix

for i in range(len(mat1)):
    for j in range(len(mat1[i])):
            print(mat1[i][j], end=' ')
    print()

for i in range(len(mat1)):
    for j in range(len(mat1[i])):
        #a, b = b, a
        if i > j :
            mat1[i][j], mat1[j][i] = mat1[j][i], mat1[i][j]
        #print(mat1[j][i])


for i in range(len(mat1)):
    for j in range(len(mat1[i])):
        #a, b = b, a
        if i > j :
            mat1[i][j], mat1[j][i] = mat1[j][i], mat1[i][j]
        #print(mat1[j][i])


print('----------------------')
for i in range(len(mat1)):
    for j in range(len(mat1[i])):
            print(mat1[i][j], end=' ')
    print()