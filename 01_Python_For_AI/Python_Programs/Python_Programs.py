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


# 11. Define a local variable inside a function and try to access it outside.
# 12. Use the `global` keyword to modify a global variable.
# 13. Create a variable name using a keyword and observe the result.
# 14. Use type hinting to declare a variable.
# 15. Create a variable and delete it using `del`, then try to print it.
# 16. Use variables in a math expression.
# 17. Create a string variable and update it using concatenation.
# 18. Print all variables from `locals()`.
# 19. Create a temporary variable using `_` and print it.
# 20. Use a variable in an f-string to print a message.