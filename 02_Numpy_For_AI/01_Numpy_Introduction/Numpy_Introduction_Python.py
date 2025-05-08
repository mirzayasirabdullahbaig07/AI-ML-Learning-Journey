# ============================
# NumPy Basics in Python
# ============================

# What is NumPy?
# NumPy is a powerful Python library used for numerical computing.
# Historically, Python was not efficient for machine learning due to performance issues.
# - C is fast but low-level and complex to program.
# - Python is easy and focuses on applications but is slower with large datasets.
# NumPy bridges the gap by combining:
# - C's speed and performance
# - Python's simplicity and ease of use

# What does NumPy provide?
# - A powerful N-dimensional array object
# - Tools for integrating C/C++ and Fortran code
# - Useful capabilities like linear algebra, Fourier transforms, and random number generation
# - Only one core data structure: the ndarray (N-dimensional array)

# Characteristics of NumPy arrays:
# - Homogeneous: all elements must be of the same type (int, float, complex)
# - Fixed size: item size is determined at the time of array creation

# To use NumPy, you need to install it first:
# pip install numpy

# Importing NumPy
import numpy as np

# ============================
# Array Creation Examples
# ============================

# 1D Array (Vector)
arr1 = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr1)
print("Type:", type(arr1))

# 2D Array (Matrix)
arr2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print("\n2D Array:\n", arr2)

# Zero Array
arr3 = np.zeros((2, 3))
print("\nZero Array (2x3):\n", arr3)

# Identity Matrix
arr4 = np.identity(6)
print("\nIdentity Matrix (6x6):\n", arr4)

# Using arange() - creates an array with a range of values
arr5 = np.arange(10)            # 0 to 9
arr6 = np.arange(5, 16)         # 5 to 15
arr7 = np.arange(5, 20, 2)      # 5 to 19 with step size 2
print("\nArange Examples:")
print("0 to 9:", arr5)
print("5 to 15:", arr6)
print("5 to 19 (step=2):", arr7)

# Using linspace() - creates an array with evenly spaced values
arr8 = np.linspace(10, 20, 10)  # 10 values between 10 and 20
print("\nLinspace (10 to 20, 10 values):\n", arr8)

# Copying an Array
arr9 = arr8.copy()
print("\nCopied Array:\n", arr9)
