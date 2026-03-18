# CONDITIONS

x = 15
if x > 5:
    print(f"{x} is greater than 5")

x = [1, 2, 3]
y = [1, 2, 3]

if x == y:
    print("True")

else:
    print("False")

a = int(input("Enter a value:"))

if a >0 :
    print(f"{a} is positive")
else:
    print(f"{a} is 0 or negative")

# Same examples for even odd

a = int(input("Enter a value:"))
if a % 2 == 0:
    print(f"{a} is even")
else:    
    print(f"{a} is odd")
 
# float values if taken, a % 2 == 0 will check only decimal part 
# and respond accordingly, for example 4.5 will be odd, 5.0 will be even

day = input("Enter a day of the week:").lower()
if day == "monday":
    print("Monday exhausts you with work")

elif day == "wednesday":      
    print("consistencies with Wednesday")

elif day == "saturday":
    print("Saturday weekend chillax!!")

else:
    print("Every day is a gift, enjoy it!!")

# PYTHON IS A CASE SENSITIVE LANG, IN CASE OF STRING CHECKING 
# UPPER OR LOWERING CASE BECOMES NECESSARY TO AVOID EXCEPTIONS

# nested if else
a = int(input("Enter a value:"))
if a > 0:
    if a % 2 == 0:
        print(f"{a} is positive and even")
    else:
        print(f"{a} is positive and odd")
else:
    print(f"{a} is not positive")

# nested if else with logical operators, showing exception handling
price = 2001

if price > 500 or price < 2000:
    print("You are eligible for discount")
    if price > 1000:
        if price > 2000:
            print("Flat 50 percent off")
        else:
            print("Flat 30 percent off")
    else:
        print("Flat 10 percent off")
else:
    print("No discount")

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

temp = int(input("Enter the temperature:"))

if temp >= 30 and temp <= 40:
    print(f"{temp} is a high !! hot day it is")
    if temp > 30:
        print("Hot alert!! Stay hydrated")

    elif temp >= 20 and temp < 30:
        print(f"{temp} is a pleasant day!! Enjoy the weather")

        if temp > 25:
            print("Might go high")
        
        elif temp == 23:
            print("Temperature is stable")

        else:
            print("Might go low")
    else:
        print(f"{temp} the current temperature is not in ideal range")

elif temp >= 20 and temp < 30:
    print(f"{temp} normal temperature")

    if temp > 25:
        print("Might go high")
    
    elif temp == 23:
        print("Temperature is stable")

    else:
        print("Might go low")

else:
    print(f"{temp} is a low !! cold day it is")

tot = int(input("Enter the amount of product:"))
city = input("Enter the city:").lower()
if city == "pune":
    if tot <= 250:
        print("Ship cost is 50")
    elif tot > 250 and tot <= 500:
        print("Ship cost is 25")
    else:
        print("Ship cost is free")

elif city == "mumbai":
    if tot <= 250:
        print("Ship cost is 75")
    elif tot > 250 and tot <= 500:
        print("Ship cost is 50")
    else:
        print("Ship cost is free")

elif city == "delhi":
    if tot <= 250:
        print("Ship cost is 100")
    elif tot > 250 and tot <= 500:
        print("Ship cost is 75")
    else:
        print("Ship cost is free")

else:
    print("We do not shipping in this city")

