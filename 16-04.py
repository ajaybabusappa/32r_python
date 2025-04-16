#Recursion


# def func():
#     func()

# func()


#Factorial 
#5! => 5 * 4 * 3 * 2 * 1
#5! => 5 * 4!
#4! => 4 * 3!
#3! => 3 * 2!
#2! => 2 * 1!

#base condition - known values



num1 = 18
temp = num1
right_prime = 'Empty'

def check_prime(input_num):
    if input_num <= 1:
        return False
    
    for i in range(2, input_num):
        if input_num % i == 0:
            return False
        
    return True


#This is for right side prime
while True:
    temp = temp + 1
    if check_prime(temp):
        right_prime = temp
        break
        
print(right_prime)

#Left prime
temp2 = num1
left_prime = 'empty'
while temp2 > 1:
    temp2 -= 1
    if check_prime(temp2):
        left_prime = temp2
        break

print(left_prime)

#13 14 17 


if left_prime == 'empty':
    print('Nearest prime is', right_prime)
elif num1 - left_prime == right_prime - num1:
    print(left_prime, right_prime)
elif num1 - left_prime < right_prime - num1:
    print(left_prime)
else:
    print(right_prime)


def fact(input_num):
    if input_num == 1:
        return 1

    print(input_num)
    return input_num * fact(input_num - 1)

#5 function on hold

#2 * 1 => 2


print(fact(5))
#5 #4 #3 #2 #1



def print_nums(input_num):
    if input_num == 0:
        return

    print(input_num)
    print_nums(input_num - 1)
    print(input_num)
    print(input_num)


print_nums(4)



# Sum of digits => 54321 => 1 + sum(5432)
# 5. Exponent
# 4. Reverse a string


def sum_digit(input_num):
    if input_num == 0:
        return 0

    return input_num % 10 + sum_digit(input_num//10)



num1 = 54321
print(sum_digit(num1))




# 5. Exponent => 5 ** 3
#a, b => a ** b
#5,3 => 5 * (5 power 2)
#5,2 => 5 * (5 power 1)

#a power b => a * (a power b-1)
# f(a, b) => a * f(a, b-1)


def exponent (a, b):
    if b == 0:
        return 1
    if b == 1:
        return a

    return a * exponent(a, b-1)

print(exponent(2, 5))

# 4. Reverse a string
#'hello' => 'o' + rev('hell')
#rev('hell') + 'o'

#'world' => 'd' + rev(worl)


def rev_str(input_str):

    if len(input_str) <= 1:
        return input_str


    return input_str[-1] + rev_str(input_str[0: len(input_str)-1])





string1 = 'hello'
print(rev_str('hello'))



#mul (a, b) => a + mul(a, b-1)
#(mul(2, 5)) => 2 + mul(2, 4)
#pow(a,b) => a * pow(a, b-1)




#Check if string is a palindrome

'MALAYALAM'

#str1
#(str1[0] == str1[-1]) and substring should be palindrome

str1 = 'MALAYALAM'

def check_palindrome(input_str):
    if len(input_str) <= 1:
        return True

    return (input_str[0] == input_str[-1]) and check_palindrome(input_str[1:-1])


print(check_palindrome(str1))




#Return maximum number in a list using recursion
list1 = [1, 10, -32, 55, 99, -100]
# fnmaximum(list1) => max(5, fnmaximum(remaining list))


def check_max(list1):
    if len(list1) == 0:
        return 'No max'

    if len(list1) == 1:
        return list1[0]

    res = check_max(list1[1:])
    if list1[0] > res:
        return list1[0]
    else:
        return res
    

print(check_max(list1))










