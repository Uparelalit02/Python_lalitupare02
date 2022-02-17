#46. Write a Python program to select the odd items of a list. list=[1,2,3,4,5,6,7,8,9]
l=list[::2]
print(l)
c=[]
#OR
for i in range(len(list)):
    if i%2 == 0:
        c.append(list[i])
print(c)