# what is oop?
# OOP is object oriented programming
# it is different style of writing code
# why oop is necessary?
# it is very practical concepts
# in python everything is object
# the problem before learning oop
# generality to specificity
# in oop u can create ur own datatypes, encapusication, abstraction, ploymorsim
# object, class, abstraction, ploymorsim, encapsulation, inheritance
# what is class?
# class is the blueprint, and object is always of some class
# e.g a mouse which is object of so many mouses
# i am an object of man, city of something

# object of which class?
a = "yasir"
print(type(a))
# the class take more code than an object takes during creation

# class contain two things
# data/property and the other is function/behaviour

# example: car is class, data of this class is no. of wheels. color
# functionality: bags, calculate milage, gps navigation


# how class looks like in python

# class car:
#     color = "blue"
#     model = "sports"
#     def calculate_milage(km, time):
#         # some code

# class name should be pascal case variable and function name must be snake_case
# what are pascal case : MirzaYasirAbdullahBaig
# camel case: mirzaYasirAbdullahBaig
# snake case: mirza_yasir_abdullah_baig

# class name-
# attribute - color, model -

# methods - gps, airbag + 
# the method which show with plus are always public
# the data which show with - are mostly private

# Object examples
# Car --- wagorR --- Object name = class name --wagorR = Car()
# Sports --- cricket --- Object name = class name --cricket = Sports()    
# Animal --- Lion --- Object name = class name --Lion = Animal()

# What are object literal
# easy way to make objects
# these are builtinclass

list1 = [1,2,3,4,5]
list2 = list() # focus on syntax object name --- class name()
print(list2) 

# ATM Machine Software in OOP


    # function vs methods
# Methods are basically functions which are written inside a class
# function is the normal function, which is not in any class


# list3 = [1,2,3,4,5,6]
# print(len(list3))  # this is a function 
# list3.append(11) # this is a method, which means this function actually defined in the list class
# print(list3)

# what is constructor
# __init__is a constructor
# constructor is a special function, which is defined inside a class(__init__) the inner code automatically excute when u create the object of the{ atm }class
# dunder method, special method, magic method

# there are so many magic method

class Atm:
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()

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
            print("Bye")

    def create_pin(self):
        self.pin = input("Enter Your PIN: ")
        print("PIN Set Successfully")

    def deposit(self):
        temp = input("Enter Your PIN: ")
        if temp == self.pin:
            amount = int(input("Enter the amount: "))
            self.balance += amount
            print("Deposit Successful")
        else:
            print("Invalid PIN")

    def withdraw(self):
        temp = input("Enter Your PIN: ")
        if temp == self.pin:
            amount = int(input("Enter the amount: "))
            if amount <= self.balance:
                self.balance -= amount
                print("Withdrawal Successful")
            else:
                print("Insufficient Funds")
        else:
            print("Invalid PIN")

    def check_balance(self):
        temp = input("Enter Your PIN: ")
        if temp == self.pin:
            print("Your balance is:", self.balance)
        else:
            print("Invalid PIN")

# Create ATM object to start
atm = Atm()
