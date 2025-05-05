# What Are Functions in Python?
# Functions are blocks of reusable code designed to perform a specific task.
# They help programmers avoid repetition, improve modularity, and enhance code readability.
# Think of functions as black boxes—you give them input, and they give you output.
# A classic example is Python's built-in print() function, which takes input and displays it as output.

# Importance of Functions
# Functions are critical in programming because:
# - They allow abstraction – hiding complexity and showing only necessary details.
# - They enable decomposition – breaking down large problems into smaller, manageable parts.

# Components of a Python Function
# 1. def keyword – used to define a function.
# 2. Function name – must be a valid identifier.
# 3. Parameters – inputs the function expects.
# 4. Docstring – a string that describes what the function does.
# 5. Body – the block of code that performs the task.
# 6. return – outputs the result of the function.
# 7. Function call – where you actually use the function with specific arguments.

# Syntax Example
def is_even(number):
    """
    This function tells if a given number is odd or even.
    Input: any valid integer
    Output: 'Odd' or 'Even'
    Created by: Mirza Yasir Abdullah Baig
    Date: 5 May 2025
    """
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Function Call:
for i in range(1, 11):
    print(is_even(i))

# Print the function’s documentation:
print(is_even.__doc__)

# Function Execution & Python Tutor Analogy
# - When the interpreter sees the def keyword, it does not execute the function immediately.
# - A global frame is created in memory for all global variables and statements.
# - When the function is called, a new local frame (like a room in a house) is created.
# - Once the function finishes, its frame is destroyed.
# - If a function doesn't explicitly return anything, Python returns None by default.

# Example:
x = is_even(4)
print(x)

# If there is no return value in a function, it returns None by default.

# Parameters vs Arguments
# - Parameters: Variables listed in the function definition.
# - Arguments: Actual values passed to the function during the call.
# Example: If `difficulty` is a parameter, then 'easy', 'medium', and 'hard' are its arguments.

# Types of Arguments in Python
# 1. Positional Arguments – Assigned based on order.
# 2. Keyword Arguments – Assigned using parameter names.
# 3. Default Arguments – Provide default values.
# 4. Arbitrary Arguments – Accept any number of arguments.

# Example: Default, Positional, and Keyword Arguments
def a_b(a=1, b=1):
    return a ** b

print(a_b(2, 3))         # Positional => Output: 8
print(a_b(2))            # Uses default for b => Output: 2
print(a_b(b=2, a=3))     # Keyword arguments => Output: 9
