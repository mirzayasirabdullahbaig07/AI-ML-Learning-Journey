# ---------------------------------------------
#  What is OOP?
# ---------------------------------------------

# OOP stands for Object-Oriented Programming.
# It is a programming paradigm based on the concept of "objects".
# OOP allows us to structure code in a way that models real-world entities more intuitively.

# ---------------------------------------------
#  Why is OOP necessary?
# ---------------------------------------------

#  More realistic and practical design
#  Makes code reusable through inheritance
#  Improves code readability and organization
#  Allows creation of custom data types (classes)
#  Encourages encapsulation and abstraction
#  Supports polymorphism — different behaviors using the same interface

# In Python, everything is treated as an object, which makes it naturally aligned with OOP.

# ---------------------------------------------
# Core OOP Concepts:
# ---------------------------------------------
# 1. Class
# 2. Object
# 3. Encapsulation
# 4. Abstraction
# 5. Inheritance
# 6. Polymorphism

# ---------------------------------------------
# What is a Class?
# ---------------------------------------------

# A class is a blueprint or template for creating objects.
# It defines properties (attributes/data) and behaviors (methods/functions) of the object.

# Example: A Car class
# - Attributes: color, model, engine_type
# - Methods: start(), stop(), calculate_mileage()

# Code Example:
# class Car:
#     color = "blue"
#     model = "sports"
#     def calculate_mileage(km, time):
#         # some logic here

# Naming Conventions:
# - Class names: PascalCase → e.g., `CarModel`, `BankAccount`
# - Variable and method names: snake_case → e.g., `calculate_mileage`

# Examples of Naming Styles:
# - PascalCase: MirzaYasirAbdullahBaig
# - camelCase: mirzaYasirAbdullahBaig
# - snake_case: mirza_yasir_abdullah_baig

# ---------------------------------------------
# What is an Object?
# ---------------------------------------------

# An object is an instance of a class.
# It has its own copy of the class's attributes and can access class methods.

# Examples:
# Car → WagonR → wagonr = Car()
# Sports → Cricket → cricket = Sports()
# Animal → Lion → lion = Animal()

# ---------------------------------------------
# Object Literals
# ---------------------------------------------

# These are built-in object types in Python like list, dict, str, etc.
# We can create their objects in two ways:
list1 = [1, 2, 3]           # Literal method
list2 = list()              # Using class constructor
print(list2)

# ---------------------------------------------
# Functions vs Methods
# ---------------------------------------------

# Function: A block of code that performs a task, defined using `def`.
# Method: A function defined inside a class and used on its objects.

# Example:
list3 = [1, 2, 3]
print(len(list3))           # len() is a function
list3.append(4)             # append() is a method (defined in list class)

# ---------------------------------------------
# What is a Constructor?
# ---------------------------------------------

# A constructor is a special method in Python used to initialize objects.
# In Python, it's defined using `__init__()` — also known as:
# - Dunder method
# - Special method
# - Magic method

# The constructor is automatically called when an object of the class is created.

# Example:
# class ATM:
#     def __init__(self):
#         print("ATM initialized")

# atm = ATM()  # This automatically calls __init__

# ---------------------------------------------
# Summary
# ---------------------------------------------

# - OOP helps model real-world behavior in code
# - Classes define the blueprint
# - Objects are instances of classes
# - Methods perform actions; attributes hold data
# - Constructors initialize object state
# - Python supports all key OOP features

# Now you’re ready to design scalable and organized software using Object-Oriented Programming!

class Atm:
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.main_menu()

    def main_menu(self):
        user_input = input("""
Welcome to the ATM System.
Please select an option:
1 - Set your PIN
2 - Make a Deposit
3 - Make a Withdrawal
4 - View Balance
5 - Exit
Enter your choice: """)
        if user_input == "1":
            self.set_pin()
        elif user_input == "2":
            self.add_funds()
        elif user_input == "3":
            self.take_cash()
        elif user_input == "4":
            self.view_balance()
        else:
            print("Thank you for using our ATM. Have a great day!")

    def set_pin(self):
        self.pin = input("Please enter a new PIN: ")
        print("Your PIN has been successfully created.")

    def add_funds(self):
        entered_pin = input("Enter your PIN to continue: ")
        if entered_pin == self.pin:
            amount = int(input("Enter the amount to deposit: "))
            self.balance += amount
            print(f"{amount} has been added to your account.")
        else:
            print("Incorrect PIN. Access denied.")

    def take_cash(self):
        entered_pin = input("Enter your PIN to continue: ")
        if entered_pin == self.pin:
            amount = int(input("Enter the amount to withdraw: "))
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawal of {amount} completed successfully.")
            else:
                print("Insufficient balance.")
        else:
            print("Incorrect PIN. Access denied.")

    def view_balance(self):
        entered_pin = input("Enter your PIN to check your balance: ")
        if entered_pin == self.pin:
            print(f"Your current balance is: {self.balance}")
        else:
            print("Incorrect PIN. Access denied.")

# Start the ATM session
atm = Atm()




# What is 'self' in Python OOP?
# 'self' represents the instance of the class. It allows access to the attributes and methods of the class in object context.
# Every instance method in a class takes 'self' as the first parameter.

# A class in Python contains:
# 1. Data (variables)
# 2. Methods (functions)

# Only objects of a class can access instance attributes and methods.
# Methods within the same class can access each other using 'self'.

class Fraction:
    def __init__(self, n, d):
        self.num = n      # numerator
        self.den = d      # denominator

    def __str__(self):
        return "{}/{}".format(self.num, self.den)

    def __add__(self, other):
        # (a/b) + (c/d) = (ad + bc) / bd
        temp_num = self.num * other.den + other.num * self.den
        temp_den = self.den * other.den 
        return "{}/{}".format(temp_num, temp_den)

    def __sub__(self, other):
        # (a/b) - (c/d) = (ad - bc) / bd
        temp_num = self.num * other.den - other.num * self.den
        temp_den = self.den * other.den 
        return "{}/{}".format(temp_num, temp_den)

    def __mul__(self, other):
        # (a/b) * (c/d) = (ac) / (bd)
        temp_num = self.num * other.num 
        temp_den = self.den * other.den 
        return "{}/{}".format(temp_num, temp_den)

    def __truediv__(self, other):
        # (a/b) / (c/d) = (a*d) / (b*c)
        temp_num = self.num * other.den 
        temp_den = self.den * other.num 
        return "{}/{}".format(temp_num, temp_den)
    

# ---------------------------------------------
# Encapsulation in Object-Oriented Programming (OOP)
# ---------------------------------------------

# What is an instance variable?
# Instance variables are variables defined inside the constructor (`__init__` method).
# These variables hold data unique to each object (instance) of the class.
# Examples: `pin`, `balance` — each object (ATM user) has its own values for these.

# Problem:
# By default, object attributes are accessible and modifiable from outside the class.
# This can lead to accidental or malicious changes — e.g., someone could change the balance to a string like "abc", which breaks the logic.

# Solution: Encapsulation
# Encapsulation is the process of hiding sensitive data to prevent unauthorized access.
# In Python, we achieve this by making attributes private using double underscores:
#   Example: self.__pin, self.__balance
# While Python does not enforce true privacy, this naming convention protects the variables from direct access.

# We expose such private variables using:
# - Getter methods (to read values)
# - Setter methods (to update values safely with validation)

# ---------------------------------------------
class Atm:
    def __init__(self):
        self.__pin = ""         # private attribute
        self.__balance = 0      # private attribute
        self.menu()
    
    # Getter for pin
    def get_pin(self):
        return self.__pin

    # Setter for pin with validation
    def set_pin(self, new_pin):
        if type(new_pin) == str:
            self.__pin = new_pin
            print("PIN changed successfully")
        else:
            print("Invalid PIN format. Must be a string.")

    # User menu
    def menu(self):
        user_input = input("""
How would you like to proceed?
1- Create PIN
2- Deposit
3- Withdraw
4- Check Balance
5- Exit
""")
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        else:
            print("Goodbye!")

    # Create PIN
    def create_pin(self):
        self.__pin = input("Enter your new PIN: ")
        print("PIN set successfully")

    # Deposit amount
    def deposit(self):
        temp = input("Enter your PIN: ")
        if temp == self.__pin:
            amount = int(input("Enter the amount to deposit: "))
            self.__balance += amount
            print("Deposit successful")
        else:
            print("Invalid PIN")

    # Withdraw amount
    def withdraw(self):
        temp = input("Enter your PIN: ")
        if temp == self.__pin:
            amount = int(input("Enter the amount to withdraw: "))
            if amount <= self.__balance:
                self.__balance -= amount
                print("Withdrawal successful")
            else:
                print("Insufficient funds")
        else:
            print("Invalid PIN")

    # Check balance
    def check_balance(self):
        temp = input("Enter your PIN: ")
        if temp == self.__pin:
            print("Your balance is:", self.__balance)
        else:
            print("Invalid PIN")

# ---------------------------------------------
# Create ATM object to start the program
atm = Atm()

# Summary of Concepts Used:
# - Need for Encapsulation
# - Private attributes (__pin, __balance)
# - Getter and Setter methods
# - Class structure and user interaction


# Reference Variables and Pass by Reference in Python

# Example 1: Reference Variable
# When you create an object and do not store it in a variable,
# you cannot access it later. It's created in memory but inaccessible.

atm = Atm()  # Object created and stored in 'atm'

# Example 2: Pass by Reference with Class Object
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

# Example 3: Object Mutability
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

# Example 4: List Mutability and ID Check

def change(L):
    print("ID inside function:", id(L))
    L.append(5)

L1 = [1, 2, 3, 4]
print("ID before function call:", id(L1))
print("List before function call:", L1)

change(L1[:])  # Pass a copy of the list (cloning)
# Permanent change is avoided due to cloning

print("List after function call:", L1)




 



