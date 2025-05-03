# What are dictionaries in python?
# Dictionaries are the keyvalue pairs in python
d1 = {"name": "yasir", "age": 24, "status": "ai-ml engineer"}
print(d1)

# Dictionaries has no indexing
# Dictionaries are mutable datatype
# keys are always immutable, values maybe mutable
# keys should be unique

# Lists sets and dictionary
# string, tuples, int, float, boolean, complex
# How to create a dictionary 

# d1 = {[1,2,3]:"Yasir"}
# print(d1) # it will through error
d11 = {(1,2,3):"Yasir"}
print(d11) # it will not through error
d2 = {"Name": "Yasir", "Name": "Abdullah"}
print(d2)

# How to create 2d dictionaries
d3 = {"Name": "Yasir","Age": 24, "Marks": {"eng": 33, "Maths": 38, "chemistry": 100}}
print(d3)

# How to access the item from the dictionary
d4 = {"name": "yasir","school": "Al-shahtah"}

print(d4["name"])
print(d4["school"])

# In dictionary there is no indexing no slicing


d5 = {"Name": "Yasir","Age": 24, "Marks": {"eng": 33, "Maths": 38, "chemistry": 100}}
print(d5["Marks"]["eng"])

# How to edit the particular item in dictionary
d6 = {"Name": "Yasir", "age": 24, "school": "fazmic"}
d6 ["Name"] = "Abdullah"
print(d6)

d7 = {"Name": "Yasir","Age": 24, "Marks": {"eng": 33, "Maths": 38, "chemistry": 100}}
d7 ["Marks"]["eng"] = 55
print(d7)

# How to add new key-value pair
d7 ["gender"] ="Male"
print(d7)
d7 ["Marks"]["Physics"] = 59
print(d7)
del d7["gender"]
print(d7)

# How to delete dictionary in python
d11 = {}
del d11

d7.clear
print(d7)


# No multiplication, no concentination
# Loops are only applicable
for i in d4:
    print(i)

# Membership
# membership only work in keys , not on values
a = {"name": "yasir"}
print("yasir" in a) # not work on keys
print("name" in a) # work on keys

# Functions in dictionary
# leng, max, min, sorted, .keys, .values