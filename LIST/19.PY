# 19. Write a Python program to get the difference between the two lists. 
list1=[1,2,3,4,5,6]
list2=[1,2,3,6,7,8]
list3=[]
for i in list1:
    if i not in list2:
        list3.append(i)
for i in list2:
    if i not in list1:
        list3.append(i)
print(list3)
    