# User Defined Functions

def greet(name):
    print(f"Hello, {name}! How are you?")

greet("Alice")
greet("Bob")

def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(f"The sum of 5 and 3 is: {result}")

def mul_table(num):
    
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

mul_table(5)


# Animal Sounds
def animal_sound(animal):
    if animal == "dog":
        return "Woof!"
    elif animal == "cat":
        return "Meow!"
    elif animal == "cow":
        return "Moo!"
    else:
        return "Unknown animal sound."

print(animal_sound("dog"))
print(animal_sound("cat"))
print(animal_sound("cow"))
print(animal_sound("lion"))


#Left aligned triangle pattern
def f1():
    num = int(input("Enter a number: "))
    print("\n")

    for i in range(1, num + 1):
        x = "*"
        print(x * i)

f1()

#Right aligned triangle pattern
def f2():
    num = int(input("Enter a number: "))
    print("\n")

    for i in range(1, num + 1):
        x = "*"
        print(" " * (num - i) + x * i)

f2()


# Factorial of a number using def 
def function(n):
    if n == 0:
        return 1

    return n * function(n - 1)

res = function(5)
print(res)
    

# ------------ KEYWORD ARGUMENTS --------------#
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

introduce(age=25, name="Alice")


# -------------Arbitrary Arguments--------------#
def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

print(multiply(2,3,4,5))

# ------------- Arbitrary Keyword Arguments --------------#
def describe_person(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

describe_person(name="Alice", age=30, city="New York")

# Combining *args and **kwargs
def mixed_args(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

mixed_args(1, 2, 3, name="Alice", age=30, city="New York", Pincode=123456)

# Return Statements
def is_even(num):
    return num % 2 == 0

result = is_even(10)
print(result)

#-------------Lambda Functions--------------#
add = lambda x, y: x + y
print(add(5, 3))


square = lambda x: x ** 2
print(square(4))

is_even = lambda num: num % 2 == 0
print(is_even(10))
print(is_even(7))

max_num = lambda a, b: a if a > b else b
print(max_num(10, 5))

min_num = lambda a, b: a if a < b else b
print(min_num(5, 10))

# Filter even numbers from a list
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)


#-------------Exception Handling--------------#

# Basic try-except block
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

try:
    n1 = 10
    n2 = 0
    result = n1 / n2
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

# File management
try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found!")
finally:
    print("This will run no matter what.")
    file.close()




