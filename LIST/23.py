# 23. Write a Python program to flatten a shallow list
list1=[['a'],['b'],['n'],['f']]
list2=[]
for i in list1:
    for j in i:
        list2.append(j)
print(list2)
