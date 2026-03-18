# # -------------Break statements--------------#
# a = [1, 3, 5, 7, 9, 11]
# val = 7

# for i in a:
#     if i == val:
#         print(f"{val} found at index {a.index(val)}")
#         break    
# else:
#     print(f"{val} not found in the list")

# for i in range(3):
#     for j in range(5):
#         if i == 1 and j == 2:
#             break
#         print(f"i : {i}, j : {j}")


# break in while
# cnt = 5
# while True:
#     print(cnt)
#     cnt -= 1
#     if cnt == 0:
#         print("Countdown complete!")
#         break


# while True:
#     user_input = input("Enter a number (or 'exit' to quit): ")
#     if user_input.lower() == 'exit':
#         break
#     print("You entered:", user_input)


## -------------Continue statements--------------#
# for val in "elephant":
#     if val == "e":
#         continue
#     print(val)

# for i in range(1, 11):
#     if i == 6:
#         continue
#     else:
#         print(i, end=" ")

# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i, end=" ")

# for i in range(10):
#     if i == 5:
#         break
#     elif i % 2 == 0:    
#         continue
#     print(i, end=" ")


## -------------Pass statements--------------#

# x = 5
# if x >= 5:
#     pass
# else:
#     print(f"{x} is less")

# for i in range(5):
#     if i == 3:
#         pass
#     else:
#         print(i, end=" ")


# # printing entire  list except number 3
# numbers = [1, 2, 3, 4, 5, 6]

# for num in numbers:
#     if num == 3:
#         pass
#     else:
#         print(num, end=" ")


# whether = "rainy"

# if whether == "rainy":
#     pass
# else:
#     print("Go out and enjoy the weather!!")

