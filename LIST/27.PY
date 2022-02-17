# 27. Write a Python program to find the second smallest number in a list. 
list1=[1,2,3,4,5]
min=list1[0]
for i in list1:
    if i>min:
        i=min
min2=list[0]
for x in list1:
    if x<min2 and x>min:
        min2=x
print(min2)

