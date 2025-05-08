# NumPy Concepts: Slicing, Indexing, and Iteration

# Slicing:
# Slicing is used to extract specific portions of arrays.
# Syntax: array[start:stop, start:stop] for 2D arrays.
# Examples:
# arr[:, 2]      -> All rows, column at index 2
# arr[:, 2:4]    -> All rows, columns 2 and 3
# arr[3:5, 1:3]  -> Rows 3 and 4, columns 1 and 2

# Indexing:
# Indexing is accessing a specific element or range in an array using its position.
# Examples:
# arr[2]       -> Access element at index 2
# arr[2:4]     -> Access elements from index 2 to 3
# arr[-1]      -> Access the last element

# Iteration:
# Iteration means looping through the array.
# Two types shown here:
# 1. Looping row-by-row: for row in array
# 2. Looping element-by-element: for element in np.nditer(array)

import numpy as np

arr1 = np.arange(24).reshape(6, 4)
arr1222 = np.arange(24).reshape(6, 4)

# I want 2 columns
print(arr1222)

# Slicing
print(arr1222[:, 2])
print(arr1222[:, 2:4])
print(arr1222[3:5, 1:3])

arr11 = np.arange(24).reshape(8, 3)  # You can reshape for all possible shapes
arr111 = np.arange(24).reshape(12, 2)

print(arr1)
print(arr11)
print(arr111)

# Indexing
arrnew = np.array([1, 2, 3, 4, 5, 6])
print(arrnew[2])     # 3
print(arrnew[2:4])   # 3 and 4
print(arrnew[-1])    # 6

# Iteration
arr_iteration = np.arange(24).reshape(6, 4)
for i in arr_iteration:
    print(i)

arr_iteration = np.arange(24).reshape(6, 4)
for i in np.nditer(arr_iteration):
    print(i)
