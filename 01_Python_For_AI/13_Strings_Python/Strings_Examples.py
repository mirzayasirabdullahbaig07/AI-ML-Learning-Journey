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



