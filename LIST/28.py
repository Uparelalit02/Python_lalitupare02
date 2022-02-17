#28. Write a Python program to find the second largest number in a list. 

list1=list(map(int,input().split(",")))


max=list1[0]

for x in list1:
    if max<x:
        max=x
        


max1=list1[0]
for x in list1:
    if x>max1 and x<max:
        max1=x

print(max1)