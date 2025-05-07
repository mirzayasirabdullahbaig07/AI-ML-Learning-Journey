### Lambda Functions in Python

# What are lambda functions?
# Lambda functions are anonymous, one-line functions defined using the 'lambda' keyword.

# Syntax: lambda arguments: expression

# Examples:
square = lambda x: x ** 2
print(square(6))  # Output: 36

add = lambda x, y: x + y
print(add(3, 5))  # Output: 8

starts_with_a = lambda x: x[0] == 'a'
print(starts_with_a("apple"))  # True
print(starts_with_a("pple"))   # False

even_or_odd = lambda x: "Even" if x % 2 == 0 else "Odd"
print(even_or_odd(4))  # Output: Even


### Why Use Lambda Functions?
# - Useful for short, throwaway functions
# - Often used with higher-order functions like map, filter, reduce
# - Makes code cleaner and concise


### Lambda vs Normal Functions
# | Feature          | Lambda Function          | Normal Function          |
# |------------------|--------------------------|--------------------------|
# | Name             | Anonymous                | Has a defined name       |
# | Syntax           | Single-line              | Multi-line               |
# | Return Statement | Implicit                 | Requires 'return'        |
# | Use Case         | Simple/one-time use      | Reusable/complex logic   |


### Higher-Order Functions
# A higher-order function either takes another function as an argument, or returns another function.

def return_sum(func, lst):
    result = 0
    for i in lst:
        if func(i):
            result += i
    return result

numbers = [11, 2, 34, 5, 56, 77, 88, 64, 4, 66, 55, 3, 46, 19]

is_even = lambda x: x % 2 == 0
is_odd = lambda x: x % 2 != 0
div_by_3 = lambda x: x % 3 == 0

print(return_sum(is_even, numbers))  # Sum of even numbers
print(return_sum(is_odd, numbers))   # Sum of odd numbers
print(return_sum(div_by_3, numbers)) # Sum of numbers divisible by 3


### Built-in Higher-Order Functions

# map(function, iterable) - Applies the function to every item in the iterable
l1 = [1, 2, 4, 5, 67, 8, 9, 7, 3]
print(list(map(lambda x: x * 2, l1)))
print(list(map(lambda x: x % 2 == 0, l1)))

# filter(function, iterable) - Filters items based on a condition
print(list(filter(lambda x: x > 4, l1)))

fruits = ["apple", "banana", "orange", "guava", "grapes"]
print(list(filter(lambda fruit: 'e' in fruit, fruits)))

# reduce(function, iterable) - Reduces iterable to a single value
import functools

l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(functools.reduce(lambda x, y: x + y, l2))           # Sum
print(functools.reduce(lambda x, y: x if x > y else y, l2)) # Max
print(functools.reduce(lambda x, y: x if x < y else y, l2)) # Min


### List Comprehensions - Alternative to map/filter
l3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

doubled = [item * 2 for item in l3]
print(doubled)

squares = [i ** 2 for i in range(10)]
print(squares)

odd_squares = [i ** 2 for i in range(10) if i % 2 != 0]
print(odd_squares)
