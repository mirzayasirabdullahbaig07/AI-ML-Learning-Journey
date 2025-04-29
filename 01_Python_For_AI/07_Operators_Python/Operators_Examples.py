# Operators are used to perform operation on variables and values in programming
# Python has some operators, we will study deeply

# 1 Arthematic Operator - ( + - * / % ** //)
# sum
a = 1
b = 3
print(a + b)
# Substraction
c = 3
d = 5
print(c - d)
# Multiplication
e = 3
f = 19
print(e * 19)
#Division
g = 12
h = 4
print(g / h)
# modelus
i = 33
j = 4
print(i%j)
# power of operator
k = 2
l = 12
print(k**l)
# Integer division
m = 44
n = 13
print(m//n)

# Comparsion Operator; These are use when u built the logic (< > == <= >= != )
ab = 3
cd = 6
print(ab > cd)
print(ab < cd)
print(ab == cd)
print(ab <= cd)
print(ab >= cd)
print(ab != cd)

#logical operator - and nor or
ac = True
bc = False
# or operators give true when any one is true, and give only false when both are false
print(ac or bc)
# and only true when both are true, otherwise false
print(ac and bc)
#not opposite of the result
print(not bc) 
print(not ac)

#bitwise operator - only work on binary values
ai = 2
ad = 5
print(ai & ad) # and operator of bitwise
print(ai | ad) # or operator of bitwise
print(ai >> ad)
print(ai << ad)
print(~ai)
print(~ad)

#Assignment operators (- += -= &= |= %= ) a++. ++a is not working in python
a3 = 5
print(a3)
r = 5
u = 5
print(r is u)

yu = "yasir"
yv = "yasir"
print(yu is yv)
print(yu is not yv)


list = [1,2,3,5]
list1 = [1,2,3,5] # in python sometimes same looking things are not same they are in different memory location
print(list is list1)

#membership operator
ya = "yasir"
print("y" in ya)
print("y" not in ya)
# we can use this operator in every datatype
