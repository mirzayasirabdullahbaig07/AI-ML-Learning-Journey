# What is Strings? Strings are sequence of characters
# In Python strings are sequence of unicode characters - Like Yasir - Y, A, S, I, R - These are characters 
# Characters are converted in unicode then unicode is converted in binary and machine only understand the binary(0, 1)

# 01 Creating String - How we create strings in Python?

a = 'Mirza Yasir Abdullah Baig' # Single inverted commas
print(a)
b = "Mirza Yasir Abdullah Baig" # Double Inverted Commas
print(b)
# Why the concepts of '' and "" commas
c = "it's raining outside" # here we use this kind of strings
print(c)
d = """yasir is an Ai developer and a machine learning expert"""
print(d)
e = '''this kind of strings are used when we write multiple lines and paragraphs best example is blogs'''
print(e)
f = str("Mirza Yasir Abdullah Baig")
print(f)

# 02 Accessing String - How we access the strings?

# Concept of Indexing in String
# Examples
name = "YASIR"
print(name)
# Output is YASIR - Every character has its own index position 0,1,2,3,4
# How to check the index position of a character
print (name[0]) # Output Y
print (name[1]) # Output A
print (name[2]) # Output S
print (name[3]) # Output I
print (name[4]) # Output R
print (name[5]) # Show error string index out of range

# Types of indexing - Positive Indexing and the other is Negative Indexing 
# In positive indexing First index is 0 and so on... 1,2,3,4 and index position left to right
# In Negative Indexing last character index position is -1 and so on -2,-3... and index position from right to left
print (name[-1]) # Output R  
print (name[-2]) # Output I  
print (name[-3]) # Output S
print (name[-4]) # Output A
print (name[-5]) # Output Y
 
# We use negative indexing when someone send u a long str and ask u to provide the last one

# Slicing is another technique
# In indexing u can only extract only one character
# In i want a character from" mirza yasir abdullah baig" i want yasir for this i use slicing
# Example for Slicing
slicestr = "Mirza Yasir Abdullah Baig"
print(slicestr[0:6]) # starting position and the end number + 1
print(slicestr[2:]) # from position 2 to onward full string
print(slicestr[:5]) # starting to position 4
print(slicestr[:]) # It will print full string
print(slicestr[0:6:2]) # from 0 to 6 index with a gap of 2 means m i will miss r and z is miss and a output will be Mra
print(slicestr[0:7:-1]) # No answer when u are doing positive indexing u cant do -1 for gap
print(slicestr[-6:-1:2]) # It will show the outcome
print(slicestr[::-1]) # It will reverse the string 
print(slicestr[-1:-7:-1]) 

# 03 Editing and Deleting String - How to edit and delete the strings in python?
# Strings are immutable, they cant be changed and cant be edit

editstr = "AI Machine Learning Journey"
editstr[0] = "x" #  It will show this error: str' object does not support item assignment
print(editstr) # You can not edit the string and dont add the string
# The question is can we reassigned the existing strings? The answer is yes

editstr = "AI Courses"
print(editstr) # You can reassign the exisiting string

del editstr
print(editstr) # This will tell there is no editstr it means it is deleted
del editstr[0] # This will not run as well 
print(editstr[2])

# 04 Strings Operators
# Arthematic Operators - In strings, we only use + and * operators

# String addition
sumstr = "Yasir" + "Baig"
print(sumstr) 
sumstr1 = "Yasir" + " " + "Abdullah"
print(sumstr1)

# Multiplication Strings 
multistr = "*"*40
print(multistr) 
multistr1 = "Yasir"*5
print(multistr1)

# Rational Operators in strings
a1 = "yasir"
b1 = "baig"
print(a1==b1)

c1 = "Abdullah"
d1 = "Mirza"
print(c1!=d1)

e1 = "Islamabad"
f1 = "kasur"
# This comparison is done by lexiographically. In dictonary, the word which comes first is smaller, and the word which comes later is bigger.
print(e1>f1)
g1 = "Yasir"
h1 = "yasir"
print(g1>h1)
# Small letters are also come later so they are big

# Logical Operators in strings
# "" - Empty strings in python are false
# Non empty strings are true
a11 = "Yasir"
b22 = "Baig"
print(a11 and b22)
print(a11 or b22)
print("" and a11)
print("" or b22)

# Loops operators in strings
loopstr = "Mirza yasir abdullah baig"
for i in loopstr:
    print(i)
# You can run all slicing on this loops operatior[0:92: or whatever]

# Membership Operators In strings
# In not in
memstr = "Mirza Yasir Abdullah Baig"
print('M' in memstr)
print('M' not in memstr)

# Functions in Strings
# Common Functions which are provided for all iterables list, tuples, str, dic, and set
# Some are only strings function

# 01 Len function in string 
str_fun = "Mirza Yasir Abdullah Baig"
print(len(str_fun))
# 02 Max function in string
print(max(str_fun)) # On the basis of accsi values
# 03 Min function in string
print(min(str_fun)) # On the basis of accsi values
# 04 Sorted function in string
print(sorted(str_fun)) # Sort the characters in ascending order
# And it will related the output in list form
# You can also get in desending order if you want
print(sorted(str_fun, reverse=True))

# Only applicable on strings
mixfuncstr = "Mirza Yasir adullah baig"
# 01 capatilize/title/uppercase/lowercase
# Capatilize the first letter of word, it wont able to change the existed string
print(mixfuncstr.capitalize())
# Title function always capatalize the each 1 letter of each word
print(mixfuncstr.title())
# Uppercase make the full string in upper. UPPER
print(mixfuncstr.upper())
# Lowercase make the small letter. LOWER, lower
print(mixfuncstr.lower())
# Swapcase - change upper to lower and lower to upper
print(mixfuncstr.swapcase())
# Count function - Tell the string of particular substring
print(mixfuncstr.count("Y")) 
# Find/index
print(mixfuncstr.find("Y")) # It tell the first occurance of substring
# if the substring is not available then it will give -1
print(mixfuncstr.index("Y")) 
print(mixfuncstr.index("LL")) # the code will crash
# The main difference between find and index is if their is no substring available then in find it will show -1 and index show error
# Always prefer find

# endswith/startswith
print(mixfuncstr.endswith("aig"))
print(mixfuncstr.startswith("Mir"))

#Format Function
formatstr = "My name is {} and i am {}, my age is {}".format("Mirza Yasir Abdullah Baig", "AI/ML Engineer",24)

formatstr = "My name is {0} and i am {1}, my age is {2}".format("Mirza Yasir Abdullah Baig", "AI/ML Engineer",24)

formatstr = "My name is {name} and i am {status}, my age is {age}".format(name = "Mirza Yasir Abdullah Baig", status = "AI/ML Engineer",age = 24)

#isalnum/isalpha/isdecimal/isdigit/isidentifier
# Use for validation and asking questions
isalnumstr = "yasir07"
print(isalnumstr.isalnum()) # Output True
isalnumstr1 = "yasir07#"
print(isalnumstr1.isalnum()) # Output False

isalphastr = "yasir"
print(isalnumstr.isalpha()) # Output True
isalphastr1 = "yasir07"
print(isalnumstr1.isalpha()) # Output False

numstr = 7
print("7".isdigit()) # True
print("7A".isdigit()) # False

identifierstr = "Yasir_Baig"
print(identifierstr.isidentifier()) # True
identifierstr1 = "Yasir-Baig"
print(identifierstr1.isidentifier()) # False

# There are so many isfunction in string for different work 

# Split function in string
# split convert the str in list
splitstr = "Mirza Yasir Abdullah Baig"
print(splitstr.split()) # ['Mirza', 'Yasir', 'Abdullah', 'Baig']
print(splitstr.split("i")) # ['M','rza', 'Yas','r', 'Abdullah', 'Ba',g']
print(splitstr.split("x")) # ["Mirza Yasir Abdullah Baig"]

# Join function in string
# It is like reverse of split
# it changes the list in str - use for urls
joinstr = ['Mirza', 'Yasir', 'Abdullah', 'Baig']
print("-".join(['Mirza', 'Yasir', 'Abdullah', 'Baig']))

# Replace function in strings
replacestr = "mirza yasir abdullah"
print(replacestr.replace("abdullah", "baig"))

# Strip - remove the spaces
stripstr = "mirza              yasir       abdullah baig"
print(stripstr.strip())








