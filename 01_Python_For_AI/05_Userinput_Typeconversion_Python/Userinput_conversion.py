# Type coversion and userinput is very important topic
# Static software: where user cannot able to talk with software: calculator
# Dynamic software: where user can able to talk with software: youtube. whatsapp
# Dynamic software requires user input

# python has builtin function is input
# input()

# input() # this is not a good practice
# input("Enter Your Name") # This is good practice, this is called prompt

# Program for 2 number and take a sum.

first_number = int(input("Enter Your First Number")) # the user input always in sting
Second_number = int(input("Enter Your Second Number")) # the user input always in sting

# why python do it. because it is univerisal format you can store anything in it

result = first_number + Second_number
print(result)

# Type function
a = type(False)
print(a)

#   Type conversion: covert datatype in to other type
# Only type conversion happens when possible
# Two types of type-conversion
 # Implicit - automatically conversion by python
 # Explicit - Manually

# example for implicit programing langauge
b = 2 +2j
print(b) # answer is 4j- here implicit programming occurs, python is smart enough to sum 2 different datatypes, one is int, other is complex

# explicit built in function - int fun, float, str, bool, list, complex, tuple, sets, only convertable
# Type conversion is not a permanent operation
# Type casting is permanent operator





