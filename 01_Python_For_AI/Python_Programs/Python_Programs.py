# 1. Print your name.
name = "Mirza Yasir Abdullah Baig"
print(name)

# 2. Print your age.
age = 24
print(age)

# 3. Print your favorite quote.
fav_quote = "I can sleep when the winds blow"
print(fav_quote)

# 4. Print the result of 5 + 7.
sum1 = 5 + 7
print(sum1)

# 5. Print your full name on one line.
full_name = "Mirza Yasir Abdullah Baig. I am AI/ML Engineer"
print(full_name)

# 6. Print your full name on two lines.
print("Mirza Yasir Abdullah Baig\nI am AI/ML Engineer")

# 7. Print a square using asterisk (*) of size 5x5.
for i in range(5):
    print("*" * 5)

# 8. Print the table of 5 using print only.
number = 5
for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")

# 9. Print a pattern using loops:
#     *
#     **
#     ***
#     ****
for i in range(1, 5):
    print("*" * i)

# 10. Print “Python is Fun!” 10 times.
for i in range(10):
    print("Python is Fun!")

# 11. Print a line with escape characters: \t \n \\
print11 = "My name is Yasir"
print(print11, "\tBaig")
print(print11, "\ni am an AI expert")
print(print11, "\\Baig")

# 12. Print a formatted address using multiple print statements.
print("My Name is Mirza Yasir Abdullah Baig")
print("Islamabad, Punjab, Pakistan")
print("House no 108, Street 100")

# 13. Print your name surrounded by stars like ***Yasir***
name_in_stars = "***Yasir***"
print(name_in_stars)

# 14. Print the type of your name using the print function.
name_type = "Mirza Yasir Abdullah Baig"
print(type(name_type))

# 15. Print a floating point number rounded to 2 decimal places.
float_num = 3.14
print(round(float_num, 2))

# 16. Print a smiley face using Unicode.
unicode_emoji = "\U0001F600"
print(unicode_emoji)

# 17. Print a triangle pattern using only print.
rows = 5
for i in range(1, rows + 1):
    print("*" * i)

# 18. Print the current year hardcoded.
current_year = 2025
print(current_year)

# 19. Print a separator line 30 dashes long.
separator = "-" * 30
print(separator)

# 20. Print a multiline string poem using triple quotes.
multiline_poem = """Twinkle twinkle little star
How I wonder what you are
Up above the world so high
Like a diamond in the sky"""
print(multiline_poem)

# 21. Declare an integer variable and print it.
int_variable = 7
print(int_variable)

# 22. Declare a float variable and print it.
float_variable = 0.7
print(float_variable)

# 23. Declare a string variable and print it.
str_variable = "Mirza Yasir Abdullah Baig"
print(str_variable)

# 24. Check the type of an integer using type().
print(type(int_variable))

# 25. Check the type of a float using type().
print(type(float_variable))

# 26. Check the type of a string using type().
print(type(str_variable))

# 27. Convert an integer to float and print it.
int_float = 8
print(float(int_float))

# 28. Convert a float to integer and print it.
float_int = 0.7
print(int(float_int))

# 29. Convert an integer to a string and print it.
int_string = 22
print(str(int_string))

# 30. Add an integer and a float and print the result.
int_one = 1
float_one = 0.8
print(int_one + float_one)

# Date: 7 May 2025

# 31. Concatenate two strings and print.
str_one = "Mirza Yasir"
str_two = "Abdullah Baig"
print(str_one + str_two)

# 32. Multiply a string 5 times and print.
mult_string = "Yasir"
print(mult_string * 5)

# 33. Create a boolean variable and print it.
bol_var = False
print(bol_var)

# 34. Use `isinstance()` to check if a variable is of type float.
check_float = 0.7
print(isinstance(check_float, float))

# 35. Declare multiple variables in one line and print them.
a = b = c = 3
print(a)
print(b)
print(c)

# 36. Swap two variables and print the result.
sawp_var1 = "Mirza"
sawp_var2 = "Yasir"
sawp_var1, sawp_var2 = sawp_var2, sawp_var1
print("sawp_var1:", sawp_var1)
print("sawp_var2:", sawp_var2)

# 37. Store a complex number and print its real and imaginary parts.
complex_num = 2 + 3j  # Corrected to a complex number
print(complex_num.real)
print(complex_num.imag)

# 38. Round a float number to 3 decimal places.
float_decimal = 1.2355
print(round(float_decimal, 3))

# 39. Format a float to show with commas (e.g., 1,000,000.50).
format_commas = 100000000
print(format(format_commas, ","))

# 40. Get the ASCII value of a character using `ord()`.
ascii_value = "Y"
print(ord(ascii_value))

# Date: 8 May 2025

# 41. Get the character from ASCII code using `chr()`.
ascii_code = 65
print(chr(ascii_code))  # Output: 'A'

# 42. Print the memory address of a variable using `id()`.
memory_of_variable = 12345
print(id(memory_of_variable))

# 43. Use f-string to print a sentence with name and age.
f_name = "Mirza Yasir Abdullah Baig"
f_age = 24
print(f"My name is {f_name} and my age is {f_age}")

# 44. Check if a float and an int are equal (like 5.0 == 5).
eql_int = 5
eql_float = 5.0
print(eql_int == eql_float)  # Output: True

# 45. Try to add a string and integer (observe error).
add_str = "Mirza Yasir Abdullah Baig"
add_int = 24
# print(add_str + add_int)  # This will cause TypeError
# Correct way:
print(add_str + str(add_int))

# ============================
# 03_Variables_Python (20 problems)
# ============================

# 46. Create a variable with your name and print it.
My_name = "Mirza Yasir Abdullah Baig"
print(My_name)

# 47. Create a variable with your age and print it.
My_age = 24
print(My_age)

# 48. Create variables of int, float, and string and print their types.
f1 = 0.7
int1 = 7
str1 = "Mirza Yasir Abdullah Baig"
print(type(f1))
print(type(int1))
print(type(str1))

# 49. Create a variable and assign it multiple times.
multi_variable = "yasir"
multi_variable = 7
multi_variable = 0.7
multi_variable = False
multi_variable = 7 + 7j
print(multi_variable)

# 50. Assign the same value to 3 variables in one line.
a1 = b1 = c1 = "Yasir"
print(a1)
print(b1)
print(c1)

# 51. Assign different values to 3 variables in one line.
a2, b2, c2 = 1, 2, 3
print(a2)
print(b2)
print(c2)

# 52. Use augmented assignment (+=) on a number variable.
plus_var = 7
plus_var += 1
print(plus_var)

# 53. Create two variables and swap their values.
var_1 = "Baig"
var_2 = "Yasir"
var_1, var_2 = var_2, var_1
print(var_1)
print(var_2)

# 54. Define a variable inside a function and print it.
def print_name():
    name = "Yasir"
    print(name)

print_name()

# 55. Define a global variable and access it inside a function.
global_var = "I am global"

def access_global():
    print(global_var)

access_global()

# Date: 9 May 2025


# 56. Define a local variable inside a function and try to access it outside.
def Globalvariable(a, b):
    abc = "yasir"  # local variable
    return a + b

# Trying to use 'abc' outside the function will cause an error
# print(abc)  # Uncommenting this will raise: NameError
print(Globalvariable(3, 5))

# 57. Use the `global` keyword to modify a global variable.
global_variable = 20

def modify():
    global global_variable
    global_variable = 10

modify()
print(global_variable)  # Output: 10

# 58. Create a variable name using a keyword and observe the result.
# The following will raise a SyntaxError because 'if' is a reserved keyword
# if = 10
# print(if)

# Correct usage:
if_var = 10
print(if_var)

# 59. Use type hinting to declare a variable.
name: str = "Yasir"
age: int = 24
height: float = 5.8
is_student: bool = True
print(name, age, height, is_student)

# 60. Create a variable and delete it using `del`, then try to print it.
var_del = "yasir"
del var_del
# print(var_del)  # Uncommenting this will raise: NameError

# 61. Use variables in a math expression.
math_var1 = 2
math_var2 = 4
print(math_var1 + math_var2)

# 62. Create a string variable and update it using concatenation.
str_con = "yasir"
str_con1 = "Baig"
str_con = str_con + " " + str_con1
print(str_con)

# 63. Print all variables from `locals()`.
print("\nLocal variables:", locals())

# 64. Create a temporary variable using `_` and print it.
_ = "temporary"
print(_)

# 65. Use a variable in an f-string to print a message.
name = "Yasir"
print(f"Hello, my name is {name} and I love Python!")

# Date 13 May 2025

# 66. Try to create a variable named `if` and observe the error.
# Invalid — 'if' is a Python keyword and cannot be used as a variable name.
try:
    exec("if = 'yasir'")
except SyntaxError as e:
    print("Error (66): Cannot use 'if' as a variable name:", e)

# 67. List all keywords in Python using the `keyword` module.
import keyword
keywords = keyword.kwlist
print("Python Keywords:", keywords)

# 68. Create valid variable names using letters and underscores.
name1 = "yasir"
_name = "yasir"
first_name = "yasir"
name_1 = "yasir"
print(name1, _name, first_name, name_1)

# 69. Create a variable starting with an underscore and print it.
_underscore_var = "yasir"
print(_underscore_var)

# 70. Create a variable with a number in it (not starting with a number).
var_num1 = 122
print(var_num1)

# 71. Try to create a variable name that starts with a number (observe the error).
# Invalid syntax — variable names cannot start with a digit.
try:
    exec("1var_num = 12354")
except SyntaxError as e:
    print("Error (71): Variable name cannot start with a digit:", e)

# 72. Use camelCase and snake_case naming and print both.
varCamel = "mirzaYasirAbdullahBaig"
var_snake = "mirza_yasir_abdullah_baig"
print(varCamel)
print(var_snake)

# 73. Check if a string is a valid identifier using `.isidentifier()`.
valid_identifier = "yasir"
print("Is valid identifier:", valid_identifier.isidentifier())

# 74. Create a variable name with a special character and observe error.
# Special characters like @ are not allowed in variable names.
try:
    exec("@yasir = 'yasir'")
except SyntaxError as e:
    print("Error (74): Variable name cannot contain special characters like '@':", e)

# 75. Explain the difference between `isidentifier()` and `isalpha()` using examples.
valid_identifier1 = "yasir"
print("isidentifier():", valid_identifier1.isidentifier())  # True
valid_isalpha = "yasir"
print("isalpha():", valid_isalpha.isalpha())  # True

# 76. Create a class with a name using PascalCase and print its type.
class YasirAbdullah:
    def __init__(self, name):
        self.name = name
obj = YasirAbdullah("yasir")
print("Type of object:", type(obj))

# 77. Use the `dir()` function to list built-in names in Python.
print("Built-in names:", dir(__builtins__))

# 78. Try assigning to a keyword and catch the SyntaxError.
try:
    exec("else = 'yasir'")
except SyntaxError as e:
    print("Error (78): Cannot assign to keyword 'else':", e)

# 79. Demonstrate how identifiers are case-sensitive in Python.
a = 5
b = 5
if a == b:
    print("a = b")
else:
    print("not equal")

# Using 'If' and 'Else' (capitalized) will cause errors.
try:
    exec("""
If a == b:
    print("a = b")
Else:
    print("not equal")
""")
except SyntaxError as e:
    print("Error (79): Python is case-sensitive. Keywords must be lowercase:", e)

# 80. Print a valid identifier that includes numbers but doesn't start with one.
valid_var = "yasir"
print(valid_var)

# Date 14 May 2025