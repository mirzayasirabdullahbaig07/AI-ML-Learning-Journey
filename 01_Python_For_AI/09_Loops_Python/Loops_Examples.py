# Loops: Loops are called iteration control block
# Repeatly same work done by loops
# Where we use loops. Loops are use to display same products
# Types of Loops. while loop, for loop

# Syntax of While Loop
# while condition:
#    code

# While Loop with Example
# When the condition false the while loop stops
number = int(input("Enter Your Number "))
i = 1
while i<11:
    print(number, "*", i, "=", number*i)
    i+= 1

# For Loops:
# range function
# Start , stop step

a = list(range(1, 11))
print(a)

b = list(range(5)) # if there is only one value then it starts with 0 to 
# start is 0 
print(b)

c = list(range(1, 11, 2)) # skipping 2 numbers
print(c)

d  = list(range(10, 0, -1)) # for negative
print(d)

# Sequence - sequence of works, "yasir", "abdullah", "baig"
# strings, lists, tuples are in sequence
# For loops work on sequence and range

for i in range(1, 10): # from 1 to 10
    print(i)

for i in range(1, 10, 2): # skiping 2 numbers
    print(i)

for i in range(10, 1, 1): # negative number  10 to 1
    print(i)

for i in "Yasir": # string
    print(i)

for i in [1,2,3,4,5]: # list
    print(i)  

for i in (1,2,3,4,5): #tuple
    print(i) 

for i in {1,2,3,4,5}: # sets
    print(i)    


# when we use for loop . when we know the number of iterations
# when we use while loop. when we dont know the number of iterations

# Nested Loops: Loops with in a loop
# Nested loops are a good option but we need sometimes use it

# Example with a astrics
# *
# **
# ***
# ****
# *****

rows = int(input("Enter the number of rows"))
for i in range(1, rows + 1):
    for j in range(0, i):
        print("*", end=" ")
    print("")    