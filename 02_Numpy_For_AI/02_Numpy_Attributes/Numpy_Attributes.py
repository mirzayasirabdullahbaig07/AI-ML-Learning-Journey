# ============================================
# NumPy Array Attributes and Important Properties
# ============================================

import numpy as np 

# --------------------------------------------
# Key Attributes of NumPy Arrays:
# - shape     : Dimensions of the array (rows, columns)
# - ndim      : Number of dimensions
# - size      : Total number of elements in the array
# - itemsize  : Size in bytes of each element
# - dtype     : Data type of the array elements
# - astype()  : Used to convert the data type of array elements
# --------------------------------------------

# 1D Array
arr1 = np.array([1, 2, 4, 5, 65, 6])
print("1D Array:", arr1)
print("Shape:", arr1.shape)           # (6,)

# 2D Array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array:\n", arr2)
print("Shape:", arr2.shape)           # (2, 3)
print("Dimensions (ndim):", arr2.ndim)
print("Total Elements (size):", arr2.size)

# 3D Array
arr3 = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])
print("\n3D Array:\n", arr3)
print("Shape:", arr3.shape)           # (2, 2, 2)
print("Dimensions (ndim):", arr3.ndim)
print("Element Size (itemsize):", arr3.itemsize, "bytes")
print("Total Elements (size):", arr3.size)
print("Data Type (dtype):", arr3.dtype)

# Changing Data Type using astype()
arr3_float = arr3.astype('float')
print("New Data Type (after astype):", arr3_float.dtype)

# Note: Using smaller data types (like float16 or int8) can reduce memory usage

# ============================================
# NumPy vs Python List: Speed & Memory Comparison
# ============================================

import numpy as np
import sys
import time

# --------------------------------------------
# Key Differences:
# - NumPy arrays are faster than Python lists
# - NumPy arrays are more memory efficient
# - NumPy arrays are more convenient for numerical operations
# --------------------------------------------

# Memory Usage Comparison
py_list = range(100)
np_array = np.arange(100)

# sys.getsizeof() returns the memory size of a single element
py_list_memory = sys.getsizeof(87) * len(py_list)
np_array_memory = np_array.itemsize * np_array.size

print("Memory used by Python list:", py_list_memory, "bytes")
print("Memory used by NumPy array:", np_array_memory, "bytes")

# --------------------------------------------
# Execution Time Comparison
# --------------------------------------------

# 1. Python List Addition
x = range(10_000_000)
y = range(10_000_000, 20_000_000)

start_time = time.time()
list_result = [(i, j) for i, j in zip(x, y)]
list_time = time.time() - start_time
print("\nExecution time using Python list:", list_time, "seconds")

# 2. NumPy Array Addition
a = np.arange(10_000_000)
b = np.arange(10_000_000, 20_000_000)

start_time_np = time.time()
array_result = a + b
array_time = time.time() - start_time_np
print("Execution time using NumPy array:", array_time, "seconds")

# --------------------------------------------
# Conclusion
# --------------------------------------------
print("\nConclusion:")
print("- NumPy arrays use less memory.")
print("- NumPy arrays execute operations significantly faster.")
print("- NumPy arrays are better for large-scale numerical computing.")
