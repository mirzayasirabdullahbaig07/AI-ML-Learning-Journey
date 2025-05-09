# Important NumPy Functions: Random Module
import numpy as np

# 1. Generate a single random float between 0 and 1
a = np.random.random()
print("Random float (0 to 1):", a)

# 2. Set the seed for reproducibility (does not return a value)
np.random.seed(1)

# 3. Generate a random float between 3 and 10
c = np.random.uniform(3, 10)
print("Random float (3 to 10):", c)

# 4. Generate 10 random floats between 3 and 100
d = np.random.uniform(3, 100, 10)
print("Random float array (3 to 100, size=10):", d)

# 5. Reshape the array into 2 rows and 5 columns
e = d.reshape(2, 5)
print("Reshaped to 2x5 matrix:\n", e)

# 6. Generate a single random integer between 1 and 10
f = np.random.randint(1, 10)
print("Random integer (1 to 9):", f)

# 7. Generate 6 random integers between 1 and 10 and reshape to 2x3
g = np.random.randint(1, 10, 6).reshape(2, 3)
print("Random integers reshaped to 2x3:\n", g)

# 8. Generate 6 random integers between 1 and 10
h = np.random.randint(1, 10, 6)
print("Random integer array (1 to 9):", h)

# Statistical operations on array h
print("Max value:", np.max(h))
print("Min value:", np.min(h))
print("Index of max value:", np.argmax(h))
print("Index of min value:", np.argmin(h))
