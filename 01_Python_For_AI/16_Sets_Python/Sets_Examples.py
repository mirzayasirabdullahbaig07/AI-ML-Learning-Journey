# -------------------------------------
# PYTHON SETS - COMPLETE EXPLANATION
# -------------------------------------

# 1. What are Sets?
# -----------------
# Sets store unique and unordered items.
# No duplicates allowed.
# No indexing, slicing, or item assignment.
# Only immutable elements can be added (int, float, str, tuple).
# Sets themselves are mutable.

# 2. Creating Sets
# ----------------

# Wrong way: creates a dictionary
s1 = {}
print(type(s1))  # Output: <class 'dict'>

# Correct empty set
s11 = set()
print(type(s11))  # Output: <class 'set'>

# Duplicates are removed
s2 = {1, 2, 4, 5, 6, 5}
print(s2)  # Output: {1, 2, 4, 5, 6}

# Mixed types allowed
s22 = {1, 2, 3, "yasir", 4.5, True}
print(s22)

# More duplicates removal
s3 = {1, 2, 3, 3, 3, 4, 5, 5, 6, 7, 7, 7}
print(s3)  # Output: {1, 2, 3, 4, 5, 6, 7}

# Error: sets cannot contain mutable types like list
# s4 = {[1, 2, 3], "Yasir"}  # TypeError

# Correct: use tuples instead
s5 = {(1, 2, 3), "Yasir"}
print(s5)

# Error: sets inside sets not allowed because sets are mutable
# s6 = {1, 2, 3, {4, 5}}  # TypeError

# Use frozenset to make inner set immutable
s6 = {1, 2, 3, frozenset({4, 5})}
print(s6)

# 3. Modifying Sets
# -----------------

# Adding elements
s44 = {1, 2, 3, 4, 45}
s44.add(32)
print(s44)

# Deleting a set
delset = {1, 2, 3, 43, 4, 45}
del delset
# print(delset)  # NameError: name 'delset' is not defined

# Removing specific element
delset1 = {1, 2, 3, 4, 5}
delset1.remove(5)  # If 5 not found, raises KeyError
print(delset1)

# Pop removes random item
popset = {1, 2, 4, 5, 56, 67, 8}
popset.pop()
print(popset)

# 4. Looping and Membership
# -------------------------

# Loop through a set
loopsets = {1, 2, 4, 5, 54, 15, 56, 6, 7}
for i in loopsets:
    print(i)

# Membership check
memsets = {"yasir", "abdullah", "baig"}
print("yasir" in memsets)  # Output: True

# 5. Built-in Functions
# ---------------------

ss1 = {1, 2, 3, 4, 5}
print(len(ss1))       # 5
print(max(ss1))       # 5
print(min(ss1))       # 1
print(sum(ss1))       # 15
print(sorted(ss1))    # [1, 2, 3, 4, 5]

# 6. Set Operations
# -----------------

A = {1, 2, 3}
B = {3, 4, 5}

# Union
print(A | B)              # {1, 2, 3, 4, 5}
print(A.union(B))

# Intersection
AB = {1, 2, 3}
BC = {2, 3, 4}
print(AB & BC)            # {2, 3}
print(AB.intersection(BC))

# Difference
A1 = {1, 2, 3}
B1 = {2, 3, 4}
print(A1 - B1)            # {1}
print(A1.difference(B1))

# Symmetric Difference
A2 = {1, 2, 3}
B2 = {3, 4, 5}
print(A2 ^ B2)            # {1, 2, 4, 5}
print(A2.symmetric_difference(B2))

# 7. Set Relations
# ----------------

# Disjoint check
A3 = {1, 2}
B3 = {3, 4}
print(A3.isdisjoint(B3))     # True

# Subset check
A4 = {1, 2}
B4 = {1, 2, 3, 4}
print(A4.issubset(B4))       # True

# Superset check
A5 = {1, 2, 3, 4}
B5 = {2, 3}
print(A5.issuperset(B5))     # True