# 14. Write a Python program to print the numbers of a specified list after removing even numbers from it. 
list1=[2,3,4,5,6,7]
for i in list1:
    if i%2==0:
        list1.remove(i)
print(list1)