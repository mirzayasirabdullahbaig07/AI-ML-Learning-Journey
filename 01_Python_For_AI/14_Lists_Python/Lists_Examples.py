# ----------------------------
# What is a list in Python?
# ----------------------------
# A list is a data type that allows us to store multiple items in a single variable.

# ----------------------------
# Difference between arrays and lists
# ----------------------------
# - Arrays are homogeneous (store only one type like all integers).
# - Lists are heterogeneous (can store different types: int, str, etc.).
# - Arrays are faster for numerical operations, but lists are more flexible.

# ----------------------------
# How to create a list in Python
# ----------------------------
l = []  # Empty list
l1 = ["yasir", 24, 3.12, True]  # Heterogeneous list
l2 = [1, 2, 3, [3, 4]]  # 2D list
l3 = [[[1, 2], [2, 3], [3, 5]], [5, 7], [5, 6]]  # 3D list
l4 = list("Yasir")  # Convert string to list: ['Y', 'a', 's', 'i', 'r']

# ----------------------------
# Accessing list items
# ----------------------------
l11 = [1, 2, 3, 4, 5]
print(l11[4])         # 5
print(l11[1:4])       # [2, 3, 4]
print(l11[::-1])      # [5, 4, 3, 2, 1]

# Accessing nested lists
l22 = [1, 2, 4, 5, [3, 4]]
print(l22[-1][1])     # 4

l33 = [[1, 2, 4, 5], [3, 8], [5, 7]]
print(l33[1][-1])     # 8

l44 = [[[1, 2], [7, 8]], [[3, 4], [5, 6]]]
print(l44[1][1][0])   # 5
print(l44[0][1][1])   # 8

# ----------------------------
# Editing a list (lists are mutable)
# ----------------------------
l424 = [1, 2, 3, 4, 5, 6, 7, 8]
l424[1] = 111
l424[-3] = 333
print(l424)  # [1, 111, 3, 4, 5, 333, 7, 8]

# Editing with slicing
l373 = [1, 2, 3, 3, 45, 6, 6, 7, 7, 8, 9]
l373[1:5] = [4, 5, 6, 6]
print(l373)  # [1, 4, 5, 6, 6, 6, 6, 7, 7, 8, 9]

# ----------------------------
# Adding new items to a list
# ----------------------------
appendlist = ["yasir", "abdullah", "baig", "ai-ml-engineer"]
appendlist.append("age is 24")
print(appendlist)

extendlist = ["yasir", "abdullah", "baig", "ai-ml-engineer"]
extendlist.extend(["age is 24", "university of lahore"])
extendlist.extend('baig')  # Adds 'b', 'a', 'i', 'g' as separate items
print(extendlist)

insertlist = ["yasir", "abdullah", "baig", "ai-ml-engineer"]
insertlist.insert(3, "Mirza")
insertlist.insert(1, "baig")
print(insertlist)

# ----------------------------
# Deleting items from a list
# ----------------------------
dellist = [1, 2, 4, 5, 6, 6, 7, 8, 8, 9, [2, 4, 6], "yasir", "baig"]
del dellist[2]         # Removes item at index 2 (value 4)
del dellist[-2:]       # Removes last two items: "yasir", "baig"
dellist.remove([2, 4, 6])  # Removes sublist
print(dellist)

# Pop (removes and returns last item)
dellist.pop()
print(dellist)
dellist.pop()
print(dellist)

# Clear (empties the list)
listclr = [1, 2, 4, 5, 6, 7, 8, 9]
listclr.clear()
print(listclr)  # []

# ----------------------------
# List Operators
# ----------------------------
lnew = [1, 2, 4, 5, 6]
lnew1 = [34, 5, 6, 7, 8]

# Concatenation
print(lnew + lnew1)

# Multiplication (repeats list)
print(lnew * 3)

# Looping through a list
for i in lnew1:
    print(i)

# Looping through list with nested item
lnew2 = [1, 2, 3, [4, 5]]
for i in lnew2:
    print(i)

# Membership check
print(4 in lnew2)  # False, because 4 is inside a sublist

# ----------------------------
# Built-in List Functions
# ----------------------------
lenglist = [1, 2, 4, 8, 4, 5]
print(len(lenglist))               # Length of the list
print(min(lenglist))               # Minimum value
print(max(lenglist))               # Maximum value
print(sorted(lenglist))            # Returns sorted list (doesn't change original)
print(sorted(lenglist, reverse=True))  # Descending order

# .sort() is permanent (modifies the list in-place)
lenglist.sort()
print(lenglist)
