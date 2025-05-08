# NumPy Array Operators and Universal Functions

import numpy as np

subarray = np.array([1, 2, 3, 4, 5, 6])
subarray1 = np.array([9, 8, 7, 6, 5, 4])

# Arithmetic operations
print(subarray - subarray1)      # Subtraction => [-8 -6 -4 -2  0  2]
print(subarray + subarray1)      # Addition => [10 10 10 10 10 10]
print(subarray * subarray1)      # Element-wise multiplication => [ 9 16 21 24 25 24]
print(subarray * 2)              # Scalar multiplication => [ 2  4  6  8 10 12]
print(subarray / subarray1)      # Division => [0.11111111 0.25       0.42857143 0.66666667 1.         1.5       ]
print(subarray % subarray1)      # Modulo => [1 2 3 4 0 2]

# Comparison operations
print(subarray > 3)              # => [False False False  True  True  True]
print(subarray < 3)              # => [ True  True False False False False]
print(subarray1 < 5)             # => [False False False False False  True]
print(subarray1 > 5)             # => [ True  True  True  True False False]

# Dot product (Matrix multiplication)
dotarray = np.arange(6).reshape(2, 3)
dotarray1 = np.arange(6, 12).reshape(3, 2)
print(dotarray.dot(dotarray1))  # => [[ 40  49]
                                 #     [112 139]]

# Aggregate functions
checkarray = np.arange(28).reshape(7, 4)
print(checkarray.max())               # => 27
print(checkarray.min())               # => 0

print(checkarray.min(axis=0))         # => [ 0  1  2  3]
print(checkarray.min(axis=1))         # => [ 0  4  8 12 16 20 24]

print(checkarray.sum())               # => 378
print(checkarray.sum(axis=0))         # => [84 91 98 105]
print(checkarray.sum(axis=1))         # => [ 6 22 38 54 70 86 102]

print(checkarray.mean())              # => 13.5
print(checkarray.mean(axis=0))        # => [12.         13.        14.        15.        ]
print(checkarray.mean(axis=1))        # => [ 1.5  5.5  9.5 13.5 17.5 21.5 25.5]

# Universal functions (ufuncs)
print(np.median(checkarray))         # => 13.5
print(np.sin(checkarray))            # => array with sine values
print(np.exp(checkarray))            # => array with exponential values
