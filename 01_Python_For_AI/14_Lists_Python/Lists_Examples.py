# What is lists in python
# Lists are datatype in which we can store multiple things at once
# What is difference between arrays and lists
# List are like array but they are different
# Array is homogenious. it means you can store only one kind of datatype like only int in the arry
# But in list you can store different datatype in same list, it is hetrogenious
# Arrays are faster and list are more programmer friendly

# How to create a list in python?
# empty list
l = []
# Hetrogenous list
l1 = ["yasir", 24, 3.12, True]
# Mulitidemensional list
#2d list
l2 = [1,2,3,[3,4]] # this is also hetrogenous list 1,2,3 is int, [3,4] is list
#3d list
l3 = [[[1,2],[3,4]],[5,6]]
l3 = [[[1,2],[2,3],[3,5]],[5,7],[5,6]]
l4 = "Yasir"

# How to Access Items in list?
l11 = [1,2,3,4,5]
print(l11[4])
print(l11[1:4])
print(l11[::-1])

# Multidemensional accessing list
l22 = [1,2,4,5,[3,4]]
print(l22[-1][1])

l33 = [[1,2,4,5],[3,8],[5,7]] # find 8
print(l33[1][-1])

