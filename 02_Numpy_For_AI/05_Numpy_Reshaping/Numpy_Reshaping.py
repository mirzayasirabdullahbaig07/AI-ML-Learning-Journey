# NumPy Array Reshaping and Manipulations

import numpy as np

# What is reshaping array?
# Reshaping means changing the shape of an array without changing its data.

# Ravel: Converts multi-dimensional array to a 1D array (flattens the array)
arrwww1 = np.array([[1, 2, 3], [4, 5, 6]])
print("Original Array:")
print(arrwww1)
print("Raveled Array:")
print(arrwww1.ravel())

# Reshape: Change the shape of the array
arrshape = np.arange(12).reshape(6, 2)
print("Reshape to 6x2:")
print(arrshape)

arrshape = np.arange(12).reshape(2, 6)
print("Reshape to 2x6:")
print(arrshape)

arrshape = np.arange(12).reshape(3, 4)
print("Reshape to 3x4:")
print(arrshape)

arrshape = np.arange(12).reshape(4, 3)
print("Reshape to 4x3:")
print(arrshape)

# Transpose: Swap rows with columns
arrtranspose = np.array([[12, 3, 4, 5], [23, 45, 6, 7]])
print("Original Array:")
print(arrtranspose)
print("Transposed Array:")
print(arrtranspose.transpose())

# Stacking: Combine multiple arrays into one
arrstack1 = np.arange(6, 12).reshape(2, 3)
arrstack2 = np.arange(12, 18).reshape(2, 3)

print("Horizontal Stack:")
print(np.hstack((arrstack1, arrstack2)))

print("Vertical Stack:")
print(np.vstack((arrstack1, arrstack2)))

# Splitting: Divide arrays into sub-arrays
arrsplit = np.arange(6, 12).reshape(2, 3)

print("Horizontal Split:")
print(np.hsplit(arrsplit, 3))

print("Vertical Split:")
print(np.vsplit(arrsplit, 2))
