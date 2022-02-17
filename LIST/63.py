# 63. Write a Python program to insert a given string at the beginning of all items in a list. 
# Sample list : [1,2,3,4], string : emp
# Expected output : ['emp1', 'emp2', 'emp3', 'emp4']
list1=[1,2,3,4]
str1="emp"
list2=[]
for i in list1:
    c=str1+str(i)
    list2.append(c)
print(list2)