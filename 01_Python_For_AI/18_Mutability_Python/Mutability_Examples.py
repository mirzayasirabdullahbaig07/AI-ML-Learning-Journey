# mutability_examples.py

# Variable and memory references
# When we create a variable, it means we're allocating memory in RAM to store some value.
# All operations and variable storage happen in RAM.

# Where is data stored in RAM?
# RAM consists of multiple registers.
# Registers are created using flip-flops, which are combinations of logic gates.
# Logic gates themselves are built from diodes and transistors.

# Memory stores both the actual value and the memory address.
# Memory addresses are represented in hexadecimal format.

# Python uses names (variables) that reference objects (values) in memory.
a = 5
print(id(a))            # Same memory address as the integer 5
print(id(5))            # Shows that 5 is stored once and reused

# In Python, everything is an object.
# Assigning one variable to another creates an alias.
b = 10
c = b
d = c
print(id(b))            # All will show the same memory address
print(id(c))
print(id(d))

# Deleting a variable only removes the reference, not the value in memory
del b
print(c)                # Still accessible via c and d

# Another concept: variable reassignment
a = 3
b = a
a = 5
print(b)                # b still holds 3, since a now references 5

# Reference Counting
import sys
a1 = "ksjhasdjfbnwsiugdhnjzbfvgagdsf"
b2 = a1
c3 = b2
print(id(a1))           # Same memory address
print(id(b2))
print(id(c3))
print(sys.getrefcount(a1))  # Returns 4: three variables + internal function call

# Garbage Collection
# If no variable references an object, Python's garbage collector will remove it
a = 2
b = a
b = None
a = None
# Now 2 is unreferenced and can be garbage collected

# Weird behavior in Python (due to memory optimization)
a22 = 1287268
b22 = a22
c22 = b22
print(sys.getrefcount(a22))  # May return a high number due to internal references

# Python caches small integers between -5 and 256
a222 = 3
b222 = 3
print(id(a222))           # Same memory address
print(id(b222))

a = 256
b = 256
print(id(a))              # Same
print(id(b))

a = 257
b = 257
print(id(a))              # Different
print(id(b))

a = -5
b = -5
print(id(a))              # Same
print(id(b))

a = -6
b = -6
print(id(a))              # Different
print(id(b))

# Why this happens: Python preloads -5 to 256 integers for optimization

# String caching
a = "Mughal"
b = "Mughal"
print(id(a))              # Same
print(id(b))

a = "Mirza yasir abdullah baig"
b = "Mirza yasir abdullah baig"
print(id(a))              # Different
print(id(b))

a = "Mirza_yasir_abdullah_baig"
b = "Mirza_yasir_abdullah_baig"
print(id(a))              # Same (valid identifier)
print(id(b))

# Lists and memory
l = [1, 2, 3]
# l is at some memory location; each element has its own address
l[2] = 1
# Updated list may reuse memory if 1 is already present elsewhere

l1 = [1, 2, 3, [4, 5]]
# List has 4 elements; [4, 5] is also a list object with its own address

# Mutability concept
# Mutable: list, set, dictionary
# Immutable: int, float, str, bool, complex, tuple

# Example with immutable data type
astr = "yasir"
print(id(astr))
astr = astr + " " + "baig"
print(id(astr))          # Different ID, new string created

# Example with mutable data type
l2 = [1, 2, 3, 4, 5]
print(l2)
print(id(l2))
l2.append(7)
print(l2)
print(id(l2))            # Same ID, value updated in-place

# Side effect of mutability
lsenior = [1, 2, 3]
ljunior = lsenior
ljunior.append(4)
print(id(lsenior))
print(id(ljunior))
print(lsenior)
print(ljunior)
# Same list object modified via both variables

# Avoid shared references using cloning
l33 = [1, 2, 3, 4]
l11 = l33[:]
print(id(l33))
print(id(l11))
l11.append(5)
print(l33)
print(l11)
# Now both lists are independent