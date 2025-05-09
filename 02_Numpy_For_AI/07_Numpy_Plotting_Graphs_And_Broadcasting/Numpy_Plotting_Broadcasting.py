# Plotting with NumPy and Broadcasting
x = np.linspace(-40, 40, 100)
print("x values:")
print(x)

y = np.sin(x)
print("sin(x) values:")
print(y)
print("Plot of sin(x):")
print(plt.plot(x, y))

y = x*x + 2*x + 6
print("Plot of x^2 + 2x + 6:")
print(plt.plot(x, y))

# Broadcasting

# Example 1
a1 = np.arange(8).reshape(2, 4)
a2 = np.arange(8, 16).reshape(2, 4)
print("Broadcasting Example 1:")
print(a1 + a2)

# Example 2
a3 = np.arange(9).reshape(3, 3)
a4 = np.arange(3).reshape(1, 3)
print("Broadcasting Example 2:")
print(a3 + a4)

# Example 3
a5 = np.arange(3).reshape(1, 3)
a6 = np.arange(12).reshape(4, 3)
print("Broadcasting Example 3:")
print(a5 + a6)

# Example 4
a7 = np.arange(4).reshape(4, 1)
a8 = np.arange(12).reshape(4, 3)
print("Broadcasting Example 4:")
print(a7 + a8)

# Example 5 (Not compatible shapes)
a9 = np.arange(3).reshape(1, 3)
a10 = np.arange(16).reshape(4, 4)
print("Broadcasting Example 5: Incompatible Shapes")
try:
    print(a9 + a10)
except ValueError as e:
    print("Error:", e)

# Example 6
a11 = np.arange(3).reshape(1, 3)
a12 = np.arange(3).reshape(3, 1)
print("Broadcasting Example 6:")
print(a11 + a12)

# Example 7
a13 = np.arange(1).reshape(1, 1)
a14 = np.arange(20).reshape(4, 5)
print("Broadcasting Example 7:")
print(a13 + a14)

# Example 8
a15 = np.arange(5)
a16 = np.arange(20).reshape(4, 5)
print("Broadcasting Example 8:")
print(a15 + a16)
