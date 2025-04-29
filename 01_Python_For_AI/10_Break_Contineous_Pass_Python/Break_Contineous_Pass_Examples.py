# Break-Contineous-Pass
# break and contineous is used with loop
# pass sometimes use with other concepts

# What Break statements do?
# if you add a break statement in the running loop it terminate the loop or break the loop, this is the functionality of break statement

# Break example
for i in range(1,10):
    if i == 5:
        break
    print(i)
 # Break is use in linear searching for example. there is 1 lac user. and u need a yasir id , you check from 0 and 1, and so on
 # let suppose yasir id is at 99 so the loops stop because you get the desired id and there is no need to continue the loop for 1 lac id.

# Continue statement is different, when the particular condition true, the particular iteration skip and the loop continues till end.

for i in range(1, 11):
    if i == 5:
        continue 
    print(i)  
# The continue statement is use when u want to display some specific thing like u are building a website and u want to display the specific product that these are in stock or out of stock then u use the continue statement

# Pass Statement is like a filler
# where we use the pass statement, when we dont know what you want to code at a specific place u use pass keyword and u continue your other code at that block, then u use pass and after creating the logic u cut the pass statement and add ur required code or logic
# You can use pass statement in functions, classes and many other places, we will discuss in our later repositories

for i in range(1, 11):
    pass
