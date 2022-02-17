# 24. Write a Python program to append a list to the second list. 
list1=[1,2,3,4,5]
list2=[]
for i in range(len(list1)):
    list2.append(list1[i])
print("list 2 is ",list2)