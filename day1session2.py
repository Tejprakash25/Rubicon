# # TUPLE

# mytup = (1, 2, "banana", True)
# print(len(mytup))
# print(type(mytup))

# print(mytup[-2])
# print(mytup[1::-1])
# print(mytup[1:-1])

# #del mytup
# #print(mytup)   #this will raise error, not defined or doesnt exist
# #convert tuple to list -> do changes -> convert list to tuple

# r = list(mytup)
# r.append(34.5)
# r.pop(4)
# tuple(r)

# print(r)


# # DICTIONARY

# dic = {"name": "abc", "age":23, "isStu": False}
# print(dic)
# print(dic["age"])

# #update : 
# dic["age"] = 26
# print(dic)

# # add new field or key value pair
# dic["city"] = "NYC"
# print(dic)

# # delete a pair
# del dic["isStu"]
# print(dic)

# # create dictionary using dict() constructor
# d2 = dict(a = "Sunflower", b = "Lily", c = "Tulip")
# print(d2)

# creating an address book using dictionary

addbook = {
    "Amit":{"ph": 57578587687, "email": "amit@example.com"},
    "Bunty":{"ph": 57578587487, "email": "bunty@example.com"},
    "Tej":{"ph": 57573387687, "email": "tej@example.com"},
    "Anit":{"ph": 57458587687, "email": "anit@example.com"}

}

# print(addbook["Bunty"]["email"], addbook["Bunty"]["ph"])

# print(addbook.copy())

# print(addbook.get("Tej"))

# print(addbook.items())

# print(addbook.keys())

print(addbook.pop("Amit"))
print(addbook)