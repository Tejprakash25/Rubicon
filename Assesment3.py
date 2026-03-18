#Sum of first 10 natural numbers

sum = 0
i = 1
while i <= 10:
    sum += i
    i += 1
print("Sum of first 10 natural number:", sum)

#Table of number

num = int(input("Enter a number:"))
i = 1
while i <= 10:
    print(num, "x", i, "=", num*i)
    i += 1

#Checking for even numbers
num = int(input("Enter number:"))
while num > 0:
    if num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is odd")
    num = int(input("Enter another number (0 to exit):"))


# Factorial :
num = int(input("Enter number:"))
a = num

factorial = 1
while num > 0:
    factorial *= num
    num -= 1
print(f"factorial of {a} =", factorial)


# Sum of even and odd numbers

start = int(input("Enteer start:"))
end = int(input("Enter end:"))

a = start

sum_even = 0
sum_odd = 0

while start <= end:
    if start % 2 == 0:
        sum_even += start
    else:
        sum_odd += start
    start+=1

print("Sum of even numbers between", a, "and", end, "is", sum_even)
print("Sum of odd numbers between", a, "and", end, "is", sum_odd)


# Prime number Check:
num = int(input("enter a number:"))

for i in range(2, num):
    if num % 2 == 0 or num % i == 0 or num < 2:
        print(f"{num} is a composite number")
        break
    else:
        print(f"{num} is a prime number")

# Classify 5 numbers as positive negtive or zero

a = 5
for i in range(a):
    num = int(input("enter numbers sequentially, press enter after each input:"))
    if num > 0:
        print("number is positive")
    elif num < 0:
        print("number is negative")
    else:
        print("number is zero")

# First 10 fibonacci numbers
x = 1
y = 1
num = 1

print(x)
print(y)
while num <= 8:
    c = x + y
    x = y
    y = c
    print(c)
    num += 1

# Reverse given number 12345 -> 54321

num = 12345
reverse = 0

while num > 0:
    mod = num % 10 
    reverse = (reverse*10) + mod
    num = num // 10

print("Reverse= ", reverse)


# Hollow square pattern
rows = 4
cols = 4
for i in range(rows):
    print()
    for j in range(cols):
        if i==0 or i==rows-1 or j==0 or j==cols-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")



# Number of vowels and consonants in given string 
string = "hello"

vowel = 0
cons = 0

for i in string:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        vowel+=1 
    else:
        cons+=1
print("Number of vowels in string:", vowel)
print("Number of consonants in string:", cons)


#Divisible by 3 and 5 from 1 to 100
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i, "is divisible by both 3 and 5")

   
# Check if palindrome using loop
number = 12399700079321
original = number
reverse = 0
temp = number

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

if original == reverse:
    print(f"{original} is a Palindrome")
else:
    print(f"{original} is NOT a Palindrome")

#for palindrome checking of string

s = "hreferh"
reversed_s = s[::-1]
if s == reversed_s:
    print(f'"{s}" is a Palindrome')
else:
    print(f'"{s}" is NOT a Palindrome')


# Using if elif else, print grades A, B, C or fail
marks = int(input("Enter your marks:"))
if marks >= 50:
    print("passed")

    if marks >= 50 and marks <= 65:
        print("Grade C")

    elif marks >= 66 and marks <= 80:
        print("Grade B")
    
    else:
        print("Grade A")
else:
    print("failed")

# Loop that finds largest number in list without using max function
numbers = [3, 7, 2, 9, 5]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print("Largest number in the list is:", largest)

# given a list of numbers, find those divisible by 3 and 5 but not by both
lis = [1, 3, 5, 6, 10, 15, 18, 20, 21, 25, 30]
div3_count = 0
div5_count = 0
for i in lis:
    if (i % 3 == 0 and i % 5 != 0):
        print(i, "is divisible by 3 but not by 5")
        div3_count += 1
    elif (i % 5 == 0 and i % 3 != 0):
        print(i, "is divisible by 5 but not by 3")
        div5_count += 1
print(div3_count)
print(div5_count)

# Multiplication table, user input
mul = int(input("Enter a number to see its multiplication table:"))
for i in range(1, 11):
    print(f"{mul} x {i} = {mul*i}")

# Prime numbers between 50 and 100
for i in range(50, 101):
    if i > 1 and all(i % j != 0 for j in range(2, i)):
        print(i, "is a prime number")

# Sum of digits of given number
num = 12345
sum_dig = 0
while num > 0:
    digit = num % 10
    sum_dig += digit
    num //=10
print("Sum of digits is:", sum_dig)

# Armstrong number between 100 and 999
for num in range(100, 1000):
    sum_cubes = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum_cubes += digit ** 3
        temp //= 10
    if num == sum_cubes:
        print(num, "is an Armstrong number")


# Nested loop to print right aligned triangle pattern
n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)
