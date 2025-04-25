# Python is a case sensitive programming language.
# keyword is a word that is reserved by a program because the word has a specific meaning. 
# keywords can be commands or parameters, every programing language has a set of keywords
# keywords cannot be used as variable names 

# python has 33 keywords
import keyword
print(keyword.kwlist)

#['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

# compilers understand these words as keyword, so dont use keyword as variables- if, as, avoid this


# Identifiers: A python identifiers is a name used to identify a variable, function, class, module or other object.

# Rules for Identifiers
   # can only start with an alphabet or _
   # Followed by 0 or  more letters, _ and digits
   # keywords cannot be used as an identifiers


name = "Mirza Yasir Abdullah Baig"  #Valid
print(name)
# 1name = "Mirza Yasir Abdullah Baig" # Invalid
# 2 = "Mirza Yasir Abdullah Baig" # Invalid
# # = "Mirza Yasir Abdullah Baig" # Invalid

name_1 = "Mirza Yasir Abdullah Baig" # Valid
print(name_1)
#False= "Mirza Yasir Abdullah Baig" #Invalid

# This is all about keywords and identifiers
