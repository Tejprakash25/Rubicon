# #Write a program to find even and odd numbers from the list and return
# #and return two seperate lists for even and odd numbers.

# a = [1,2,3,4,5,6,7,8,9,10]
# eve = []
# odd = []

# for i in a:
#     if i % 2 == 0:
#         eve.append(i)
#     else:
#         odd.append(i)

# print(eve)
# print(odd)

# Find the armstrong number between 1 to 100

# a = []
# for i in range(1, 100):
#     sum = 0
#     temp = i
#     while temp > 0:
#         digit = temp % 10
#         sum += digit ** 3
#         temp //=10
#         if i == sum:
#             a.append(i)
          
# print(a) ## NOT SOLVED YET

#--------------------------------------------------------------
#--------------------------------------------------------------
# # String values to array elements
# x = input("Enter numbers with spaces:")
# x = x.split()
# print(x) ... # ['1', '2', '3', '4', '5']


# new_x = list(map(int, x))
# print(new_x) ... # [1, 2, 3, 4, 5]

# # Single string value to array element
# x = '4567'
# x = x.split()
# print(x) ... # ['4567']

# x = '4 5 6 7'
# x = x.split()
# print(x) ... # ['4', '5', '6', '7']

# x = '4 5,6 7'
# x = x.split(',')
# print(x) ... # ['4 5', '6 7']

# # Sum of those converted array elements

# x = input("Enter numbers with spaces:")
# x = x.split()

# new_x = list(map(int, x))
# print(new_x)
# print(sum(new_x))

# # def function for the same
# def convert():
#     x = input("Enter numbers with spaces: ")
#     x = x.split()

#     new_x = list(map(int, x))
#     print(new_x)

# convert()



## even funtion for converted values
# def even(n):
#     return int(n) % 2 == 0
    
# x = input("Enter numbers with spaces: ")
# x = x.split()

# eve = list(filter(even, map(int, x)))
# # or ... eve = list(filter(even, x) for ['2','4',]..

# print(eve)




## Module is a python file with .py extension which contains python code. 
# It can be imported in other python files to use the functions and variables defined in it. 
# and packages are the collection of modules. ##




## reduce function for sum of converted values
# from functools import reduce

# def add(a,b):
#     return a+b

# x = [1,2,3,4]
# n = reduce(add,x)
# print(n)

def mult(a,b):
    return a*b

def sqr(a):
    return a*a

def cube(a):
    return a*a*a


