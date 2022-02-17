# 7. Write a Python program to remove duplicates from a list. 
list=['a','b','b','c','c','d']
list1=set(list)
print(list1)

#or 
res=[]
for i in list:
    if i not in res:
        res.append(i)
print(res)

    