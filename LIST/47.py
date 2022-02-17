# 47. Write a Python program to insert an element before each element of a list. 
list=['a','b','c','d']
letter='t'
new_list=[]
for i in list:
    new_list.append(letter)
    new_list.append(i)
print(new_list)
 