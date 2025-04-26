# Literals: These are the raw data given to the variabe. 
# In python, there are four type of literals
# Numerical - string - Boolean - Special

# 01 Numeric literals
a = 0b1010 #binary literals
b = 100 # decimal literals
c = 0o310 #octal literals 
d = 0x12c #hexadecimal literals

# float literals
float_1 = 10.5
float_2 = 1.5e2
float_3 = 1.5e-3

#complex literals
x = 3.14j

print(a,b,c,d)
print(float_1, float_2, float_3)
print(x, x.imag, x.real)

# string literals
name = 'yasir'
name = "yasir"
name = """yasir""" # for multiple lines

# Boolean Literals
a1 = True + 4
b1 = False + 10

print("a:", a1)
print("b:", b1)

#special literals
a2 = None # absense of anything
print(a2)
# None is used when we create a variable and we can use it in future but not now.