# -------------------------
# What Are Tuples in Python?
# -------------------------
# Tuples are similar to lists, but with one key difference:
# Tuples are immutable — once created, their content cannot be changed.
# In this section, we will learn about creating, accessing, deleting, and using tuples.

# -------------------------
# How to Create a Tuple
# -------------------------
tuple1 = ()
print(tuple1)  # Empty tuple

tuple2 = (1, 2, 3, 4)
print(tuple2)

tuple3 = (1, 2, 3, "Yasir", True)
print(tuple3)  # Heterogeneous tuple

# -------------------------
# Creating a Single Item Tuple
# -------------------------
tuple4 = (1,)  # Must include a comma
print(tuple4)

tuple5 = tuple("Yasir")  # From string to tuple of characters
print(tuple5)  # ('Y', 'a', 's', 'i', 'r')

tuple6 = tuple([1, 2, 3, 4, 5, 6])  # From list
print(tuple6)

# -------------------------
# Accessing Tuple Elements
# -------------------------
tuple11 = (1, 2, 3, 5, 6)
print(tuple11[1])    # 2
print(tuple11[-2])   # 5

tuple22 = (1, 2, 3, (4, 5))  # Nested tuple
print(tuple22[-1][0])  # 4

# -------------------------
# Editing Tuples
# -------------------------
# Tuples are immutable — we cannot modify, add, or delete elements inside them.
# However, we can delete the entire tuple variable.

deltuple = (1, 2, 3, 4, 5)
print(deltuple)
# del deltuple  # Uncommenting this would delete the variable

# -------------------------
# Tuple Operations
# -------------------------
tup1 = (1, 2)
tup2 = (3, 4)

# Concatenation
print(tup1 + tup2)  # (1, 2, 3, 4)

# Repetition
print(tup1 * 2)     # (1, 2, 1, 2)
print(tup2 * 3)     # (3, 4, 3, 4, 3, 4)

# Looping through a tuple
for i in tup1:
    print(i)

# Membership Operators
print(1 in tup1)         # True
print(3 in tup1)         # False
print(1 not in tup1)     # False

# -------------------------
# Tuple Functions
# -------------------------
functup = (1, 2, 2, 4, 54, 65, 6)

print(len(functup))               # Number of elements
print(min(functup))               # Minimum value
print(max(functup))               # Maximum value
print(sorted(functup))            # Returns a sorted list
print(sorted(functup, reverse=True))  # Sorted in descending order

# -------------------------
# Summary
# -------------------------
# Tuples are read-only data types (immutable)
# Lists are read-write data types (mutable)
# Tuples are useful for data integrity and when the structure should not change
