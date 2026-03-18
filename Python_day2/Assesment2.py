# # create a tuple with 5 elements
# tup = (23, 45, 82, 71, 69)

# # python fuction to return even values
# def evenum(tup):
#     for i in range(len(tup)):
#         if tup[i] % 2 == 0:
#             print(tup[i])
    
# evenum(tup)

# unpacking of elements

# x = (23, 45, 67)
# a,b,c= x
# print(a)
# print(b)
# print(c)
# #or

# a,b,c = (23, 45, 67)

# # Concatenate two tuples
# a = (1, 2, 3)
# b = (4, 5, 6)

# c = a + b
# print(c)

# Min max function in tuple
# a = (34, 21, 1, 45)

# def minmax(a):
#     print(min(a))
#     print(max(a))
        
# minmax(a)

# set operations (union, intersection, diff)

# A = {17, 34, 2, 81}
# B = {29, 5, 17, 7}

# print(A.union(B))
# print(A.intersection(B))
# print(A-B)

# Dictionary subject : marks

# dic = {"oop": 67, "dbms":80, "cns":34, "m3": 77}
# # def Dict(dic):
# #     for key in dic:
# #         print(dic[key])

# def Dict(dic):
#     for key in dic:
#         if dic[key] > 50:
#             print(dic[key])

# Dict(dic)

# Given a set of strings, remove the words starting from "a",
#  and return updated set

# strset = {"apple", "banana", "grapes", "avocado", "orange"}

# for word in list(strset):
#     if word[0] == "a":
#         strset.remove(word)

# print(strset)
