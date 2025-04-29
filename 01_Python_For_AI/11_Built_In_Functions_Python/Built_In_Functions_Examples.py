# 01 Print Function
# Use to Print anything
print("Mirza Yasir Abdullah Baig")

# 02 Input Function
# Use to take user input, the datatype always of string type so we use int, which is called type conversion
input("Enter Your Name")
 # 03 Type Function
 # Use to pridict the data type of any variable
a = "Mirza Yasir Abdullah Baig"
print(type(a))
b = 100
print(type(b))
c = 0.76
print(type(c))
d = False
print(type(d))

# 04 Type coversion function
e = int("5")
print(e)

f = int(0.5)
print(f)

# 05 Absolute Function use in machine learning domain
ab = abs(5)
print(ab)

ac = abs(-5)
print(ac)

# 06 Power Function
pw = pow(2, 3)
print(pw)

# 07 Min/max Function
minmax = ([124,2,5,6,7,8,7])
print(min(minmax))
print(max(minmax))
# U can also use on string
minstr = "Mirza"
print(min(minstr))
print(max(minstr))# This is calculated on the basis of ascii values

# 08 Round Function
decvalue = 222/9
print(round(decvalue, 2)) # answer will be . 22 or something

# 09 divmod Function : it gives 2 result integer devision and modulus
print(divmod(5, 2)) # (2, 1)
print(divmod(11, 4)) # (2, 3)

# 10 bin/oct/hex - use to get binary value, octal or hexal values
binvalue = 5
print(bin(binvalue))
octvalue = 13
print(oct(octvalue))
hexvalue = 29
print(hex(hexvalue))

# 11 Id Function - use to check the address of a variable stored in your computer
idfunc = 5
print(id(idfunc))

# 12 ord Function
# When we need the asscii values we use this function
ordfunc = 'y'
print(ord(ordfunc))
ordfunc1 = "b"
print(ord(ordfunc1))

# 13 Length Function
# check the length of any 
lenfunc = [1,2,3,4,5,6]
print(len(lenfunc))

# 14 SUM Function
sumfunc = (1,3,4,5,6,76,7)
print(sum(sumfunc))

# 15 Help Function - read any detail of the function
help("sum")






