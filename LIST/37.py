# 37. Write a Python program to find common items from two lists. 
list1=[1,2,3,4,5,6,7,5]
list2=[2,3,4,1,3,9,8,5]
list3=[]
for i in list1:
    for j in list2:
        if i==j:
            list3.append(i)
print(set(list3))