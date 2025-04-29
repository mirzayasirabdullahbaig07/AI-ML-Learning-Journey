# What are Modules?
# Consider a module to be same as a code library 
# A file containing a set of functions you want to include in your application
# Examples of python modules - Math, Random, OS, Time

# Math Modules

import math
a = math.e
print(a)
b = math.factorial(7)
print(b)
c = math.pi
print(c)
d = math.sqrt(59)
print(d)

# Random Module
import random
f = random.randint(1, 100)
print(f)

shuff = [1,2,3,4,5,6,7]
random.shuffle(shuff)
print(shuff)

# Time Module
import time
tim = time.time()
print(tim)

tim1 = time.ctime()
print(tim1)

delay1 = "Mirza Yasir"
print(delay1)
time.sleep(2)
delay2 = "Abdullah Baig"
print(delay2)

# OS Module

import os
acurrent = os.getcwd
print(acurrent)
acurrent2 = os.listdir()
print(acurrent2)