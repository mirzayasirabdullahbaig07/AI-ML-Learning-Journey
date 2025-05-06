# ----------------------------
# Introduction to Recursion
# ----------------------------

# What is recursion?
# A function that calls itself is called recursion.
# Recursion is mostly used in interviews to test problem-solving skills.
# In real projects, loops are often preferred because recursion can be inefficient if not optimized.

# Two essential parts of recursion:
# 1. Base Case – the condition where recursion stops.
# 2. Recursive Step – break the larger problem into smaller pieces.

# -------------------------------------
# Example 1: Multiply using recursion
# -------------------------------------
def mul(a, b):
    if b == 1:
        return a
    else:
        return a + mul(a, b - 1)
print("Multiplication (4 * 6):", mul(4, 6))


# --------------------------------
# Example 2: Factorial Function
# --------------------------------
def fact(number):
    if number == 1:
        return 1
    else:
        return number * fact(number - 1)
print("Factorial (5!):", fact(5))


# ------------------------------------------
# Example 3: Palindrome using Recursion
# ------------------------------------------
# A palindrome reads the same forward and backward (e.g., madam).
def pel(text):
    if len(text) <= 1:
        print(f"'{text}' is a palindrome")
    else:
        if text[0] == text[-1]:
            pel(text[1:-1])
        else:
            print(f"'{text}' is not a palindrome")

pel("madam")
pel("malayam")
pel("yasir")


# -------------------------------------------------------
# Example 4: Rabbit Problem (Fibonacci using Recursion)
# -------------------------------------------------------
# Problem: How many rabbits after 'm' months?
# Each pair reproduces every month after 1 month old, never dies.

# Naive recursive Fibonacci
def fib(m):
    if m == 0 or m == 1:
        return 1
    else:
        return fib(m - 1) + fib(m - 2)
print("Rabbits after 12 months (slow):", fib(12))

# Optimized using Memoization (Dynamic Programming)
def memo(m, d):
    if m in d:
        return d[m]
    else:
        d[m] = memo(m - 1, d) + memo(m - 2, d)
        return d[m]
d = {0: 1, 1: 1}
print("Rabbits after 48 months (fast with memo):", memo(48, d))


# ---------------------------------------------------
# Example 5: Generate All Subsets (Power Set)
# ---------------------------------------------------
# Input: [1, 2, 3]
# Output: [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
def generate_subsets(nums):
    result = []
    def backtrack(index, current):
        if index == len(nums):
            result.append(current[:])
            return
        # Exclude the current number
        backtrack(index + 1, current)
        # Include the current number
        current.append(nums[index])
        backtrack(index + 1, current)
        current.pop()  # backtrack
    backtrack(0, [])
    return result
nums = [1, 2, 3]
print("All subsets of [1, 2, 3]:", generate_subsets(nums))
