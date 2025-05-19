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

# Date 12 May 2025

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

# Date 13 May 2025


# 81. Take user input for name and print a greeting.
greeting_input = input("Enter your name: ")
print("Hello, " + greeting_input + "!")

# 82. Take two numbers as input and print their sum.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Sum:", num1 + num2)

# 83. Take input and check its type.
input_checker = input("Enter something: ")
print("Data type:", type(input_checker))

# 84. Take a float input and convert it to int.
float_input = float(input("Enter a float number: "))
print("Integer:", int(float_input))

# 85. Take an int input and convert it to float.
int_input = int(input("Enter an integer: "))
print("Float:", float(int_input))

# 86. Take string input and convert to list of characters.
string_input = input("Enter a string: ")
print("List of characters:", list(string_input))

# 87. Take age as input and print "Adult" or "Minor".
person_age = int(input("Enter your age: "))
if person_age >= 18:
    print("Adult")
else:
    print("Minor")

# 88. Take two inputs and swap their values.
a = input("Enter first value (a): ")
b = input("Enter second value (b): ")
a, b = b, a
print("After swapping: a =", a, ", b =", b)

# 89. Take a number and convert it to binary.
num_binary = int(input("Enter a number: "))
print("Binary:", bin(num_binary))

# 90. Take a number and convert it to octal.
num_octal = int(input("Enter a number: "))
print("Octal:", oct(num_octal))

# Date 14 May 2025


# 91. Take a number and convert it to hexadecimal.
num_hexa = int(input("Enter your number: "))
print("Hexadecimal:", hex(num_hexa))

# 92. Take name and age from user and print formatted sentence using f-string.
user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))
print(f"The person's name is {user_name} and the age is {user_age}.")

# 93. Take height and weight from user and calculate BMI.
patient_height = float(input("Tell me your height in meters: "))
patient_weight = float(input("Tell me your weight in kilograms: "))
bmi = patient_weight / (patient_height ** 2)
print(f"The patient's BMI is: {bmi:.2f}")

# 94. Take temperature in Celsius and convert to Fahrenheit.
celsius = float(input("Enter the temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")

# 95. Take hours and rate/hour and calculate total salary.
total_hours = float(input("Enter total hours worked: "))
rate_hour = float(input("Enter the rate per hour: "))
total_salary = total_hours * rate_hour
print(f"Total salary is: {total_salary:.2f}")

# 96. Take marks in 5 subjects and print the average.
mark1 = float(input("Enter Maths marks: "))
mark2 = float(input("Enter English marks: "))
mark3 = float(input("Enter Physics marks: "))
mark4 = float(input("Enter Chemistry marks: "))
mark5 = float(input("Enter Biology marks: "))
total_marks = mark1 + mark2 + mark3 + mark4 + mark5
average_of_student = total_marks / 5
print(f"Average marks: {average_of_student:.2f}")

# 97. Take a number and check if it is even or odd.
number_checker = int(input("Enter the number: "))
if number_checker % 2 == 0:
    print("It is even.")
else:
    print("It is odd.")

# 98. Ask user to enter a password and mask it (just simulate masking).
password = input("Enter your password: ")
masked_password = '*' * len(password)
print(f"Your password is: {masked_password}")

# 99. Take date of birth and calculate current age (hardcode current year).
hardcode_year = 2025
birth_year = int(input("Enter your birth year: "))
current_age = hardcode_year - birth_year
print(f"Your age is: {current_age} years.")

# 100. Ask user a yes/no question and convert response to lowercase.
response = input("Do you want to continue? (yes/no): ")
response_lower = response.lower()
print(f"Your response in lowercase: {response_lower}")

# Date 15 May 2025

# 101. Input a number and round it to 2 decimal places.
round_num = float(input("enter a number"))
print(round(round_num, 2))

# 102. Ask for a number and print its square and cube.
nums = int(input("Enter a number: "))
print("Square:", nums ** 2)
print("Cube:", nums ** 3)

# 103. Input a sentence and count how many words it has.
input_sentence = input("enter the sentence")
wordss = input_sentence.split()
print(wordss)

# 104. Take a single character input and print its ASCII value.
char = input("Enter a single character: ")
if len(char) == 1:
    print("ASCII value:", ord(char))
else:
    print("Please enter only one character.")

# 105. Convert a string input to boolean.
str_boolean = "yasir"
print(bool(str_boolean))

# 106. Take a number and check if it is positive, negative or zero.
num_check = int(input("enter the number"))
if num_check == 0:
    print("it is zero")
elif num_check > 0:
    print("it is positive")
else:
    print("number is negative")

# 107. Ask for a number and convert it to float safely using try-except.
try:
    num = input("Enter a number: ")
    float_num = float(num)
    print("Converted to float:", float_num)
except ValueError:
    print("Invalid input! Please enter a valid number.")

# 108. Take an integer input and print all digits separately.
number = input("Enter a number: ")
for digit in number:
    print(digit)

# 109. Ask for a full name and print the initials.
full_name = input("Enter your full name: ").strip()
words = full_name.split()
initials = ""
for word in words:
    initials += word[0].upper()  # Take first letter and capitalize it
print("Initials:", initials)

# 110. Input a value and check whether it's digit, alpha, or alphanumeric.
value = input("Enter a value: ")
if value.isdigit():
    print("The value is all digits.")
elif value.isalpha():
    print("The value is all alphabetic.")
elif value.isalnum():
    print("The value is alphanumeric.")
else:
    print("The value contains special characters or spaces.")

# 16 May 2025

# 111. Print the string literal "Hello, World!".
print("Hello, World")

# 112. Define a string literal and print its type.
string_literal = "This is string literal"
print(type(string_literal))

# 113. Define a float literal and print it.
float_literal = 0.7
print(float_literal)

# 114. Define an integer literal and print it.
int_literal = 12345
print(int_literal)

# 115. Define a boolean literal and print it.
boolean_literal = True
print(boolean_literal)

# 116. Define a complex number literal and print its real and imaginary parts.
complex_number = 2 + 2j
print("Real part:", complex_number.real)
print("Imaginary part:", complex_number.imag)

# 117. Print a list literal containing 3 integers.
list_literal = [1, 2, 3]
print(list_literal)

# 118. Define and print a tuple literal containing 3 different data types.
tuple_literal = (1, "hello", 3.14)
print(tuple_literal)

# 119. Define a set literal containing 5 unique elements.
set_literals = {"yasir", "abdullah", 23, True, False} 
print(set_literals)

# 120. Define a dictionary literal with 3 key-value pairs and print it.
dictionary_literals = {"name": "yasir", "fullname": "abdullah", "age": 23} 
print(dictionary_literals)

# 121. Print a string literal containing escape characters like \n, \t.
str_escape = "This is a string with escape characters:\nNew Line\tTabbed Text"
print(str_escape)

# 122. Define a multi-line string literal and print it.
multi_line_string = """My name is Yasir and I am a machine learning engineer.
My age is 24.
I want to do a job."""
print(multi_line_string)

# 18 May 2025


# Reference Variables and Pass by Reference in Python

# 123. Reference Variable
# When you create an object and do not store it in a variable,
# you cannot access it later. It's created in memory but inaccessible.

atm = Atm()  # Object created and stored in 'atm'

# 124. Pass by Reference with Class Object
class Customer:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

def greet(customer):
    if customer.gender == "Male":
        print("Hello", customer.name, "sir")
    else:
        print("Hello", customer.name, "mam")
    cust2 = Customer("Baig", "Male")
    return cust2

cust = Customer("Mirza", "Male")
new_cust = greet(cust)
print(new_cust.name)

# When you pass a class object to a function,
# the parameter becomes a reference to the same object.
# So both 'customer' and 'cust' refer to the same object in memory.

# In Python, everything is an object.
# You can pass lists, sets, dicts, strings, and even custom class objects to functions.

# 125. Object Mutability
class Customer:
    def __init__(self, name):
        self.name = name

def greet(customer):
    print("ID inside function before change:", id(customer))
    customer.name = "Yasir"  # Changes the original object
    print("Name inside function:", customer.name)
    print("ID inside function after change:", id(customer))

cust = Customer("Mirza")
print("ID before function call:", id(cust))
greet(cust)
print("Name after function call:", cust.name)

# Output:
# ID remains the same throughout, showing that the object is mutable
# The name is changed to 'Yasir', reflecting the change outside the function

# 126. List Mutability and ID Check

def change(L):
    print("ID inside function:", id(L))
    L.append(5)

L1 = [1, 2, 3, 4]
print("ID before function call:", id(L1))
print("List before function call:", L1)

change(L1[:])  # Pass a copy of the list (cloning)
# Permanent change is avoided due to cloning

print("List after function call:", L1)

# 127. Define an integer literal with an underscore to make it more readable
int_underscore = 1_00_0000
print("127:", int_underscore)

# 128. Convert a binary literal (e.g., 0b101) to decimal and print it
binary_literal = 0b101
print("128:", int(binary_literal))

# 129. Convert an octal literal (e.g., 0o15) to decimal and print it
octal_literal = 0o15
print("129:", int(octal_literal))

# 130. Convert a hexadecimal literal (e.g., 0x1F) to decimal and print it
hex_literal = 0x1F
print("130:", int(hex_literal))

# 131. Use a floating-point literal with scientific notation (e.g., 1e3) and print it
sci_notation = 1e3
print("131:", sci_notation)

# 132. Use a boolean literal in an if statement and print a message based on its value
flag = True
if flag:
    print("132: Flag is True")
else:
    print("132: Flag is False")

# 133. Demonstrate an invalid literal error by trying to create an incorrect literal
# Uncommenting the below line will raise a ValueError
# invalid = int("abc")
# print("133:", invalid)

# 134. Print a string literal with special characters inside (like quotes inside a string)
quote_str = "He said, \"Python is awesome!\""
print("134:", quote_str)

# 135. Use complex numbers and print real and imaginary parts
complex_num = 4 + 5j
print("135: Real part:", complex_num.real, ", Imaginary part:", complex_num.imag)
