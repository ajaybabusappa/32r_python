print('Patterns')

n = 5

# for i in range(n):
#     print('* ' * 5)


for i in range(n):
    for j in range(n):
        if i >= j:
            print('*', end=' ')
    print()

# print(3, end='')
# print(5)
# print(6)





print('-------------------------')

for i in range(n):
    for j in range(n):
        if i <= j:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()



print("--------")

n = 9

for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == n-1 or j == n-1 or i == j or i +j == n-1:
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()



print("Alphabets")

#Alphabets

mid = n//2
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or  i == n-1 or (i == mid and j > mid) or (j == n-1 and i > mid):
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()

    




for i in range(n):
    start = 1
    for j in range(n):
        if i >= j:
            print(start, end=' ')
            start += 1
    print()


#0
#0 1
#0 1 0
#0 1 0 1
#0 1 0 1 0




#0
#1 0
#0 1 0
#1 0 1 0



for i in range(n):
    if i % 2 == 0:
        start = 0
    else:
        start = 1
    for j in range(n):
        if i >= j:
            print(start, end=' ')
            if start == 0:
                start = 1
            else:
                start = 0
    print()




#Alphabetic patterns - ascii or unicodes

print(chr(97))
print(chr(122))


print(ord('A'))
print(ord('['))


n = 4
start = 65
for i in range(n):
    for j in range(n):
        if i >= j:
            print(chr(start), end=' ')
            start += 1
    print()        