#T.C and S.C

#T.C
n = 25 #100 #1000


sum = 0
for i in range(1, n + 1): #25
    sum += i

print(sum)
#linear time complexity code - O(n)


#Method 2
print((n*(n+1))//2) #3 or 1
#O(1)





#
n = 20 #40 #60
for i in range(0, n): #400 #1600 #3600
    for j in range(0, n):
        print("Something")


#O(n square)

#O(n cube)


#O(1) O(n) O(n square) O(n cube)

#log(n) < n
#O(log(n))
#O(nlogn)


#Efficiency:O(1) > O(logn) > O(n) > O(nlogn) > O(n square) > O(n cube)

num1 = 17 #43 #44

for i in range(2, num1): #15 #41 => O(n) #Even number O(1)
    if num1 % i == 0:
        print("Not prime")
        break




#

for i in range(1, 25): #O(n square)
    for j in range(1, 25):
        print("Nothing")
    

for i in range(1, 25): #O(n)
    print("Okay")


#O(n square + n) => O(n square)


#Space complexity - Additional memory

#O(1), O(n)


#O(1) - s.c  =>  Input increase 


sum = 0
for i in range(1, n + 1): #25
    sum += i

print(sum)
#linear time complexity code - O(n)
#s.c - O(1)


#Method 2
print((n*(n+1))//2) #3 or 1
#O(1)
#O(1) - s.c


#list1 = [245, 678, 901, 333]
#output = [11, 21, 10, 9]



