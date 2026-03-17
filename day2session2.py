# # CONDITIONS

# x = 15
# if x > 5:
#     print(f"{x} is greater than 5")

# x = [1, 2, 3]
# y = [1, 2, 3]

# if x == y:
#     print("True")

# else:
#     print("False")

# a = int(input("Enter a value:"))

# if a >0 :
#     print(f"{a} is positive")
# else:
#     print(f"{a} is 0 or negative")

# Same examples for even odd

# a = int(input("Enter a value:"))
# if a % 2 == 0:
#     print(f"{a} is even")
# else:    
#     print(f"{a} is odd")
 
# float values if taken, a % 2 == 0 will check only decimal part 
# and respond accordingly, for example 4.5 will be odd, 5.0 will be even

# day = input("Enter a day of the week:").lower()
# if day == "monday":
#     print("Monday exhausts you with work")

# elif day == "wednesday":      
#     print("consistencies with Wednesday")

# elif day == "saturday":
#     print("Saturday weekend chillax!!")

# else:
#     print("Every day is a gift, enjoy it!!")

#PYTHON IS A CASE SENSITIVE LANG, IN CASE OF STRING CHECKING 
#UPPER OR LOWERING CASE BECOMES NECESSARY TO AVOID EXCEPTIONS

# nested if else
a = int(input("Enter a value:"))
if a > 0:
    if a % 2 == 0:
        print(f"{a} is positive and even")
    else:
        print(f"{a} is positive and odd")
else:
    print(f"{a} is not positive")