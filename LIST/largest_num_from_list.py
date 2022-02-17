list=[2,3,4,5,6]
max=list[0]

for x in list:
    if max<x:
        max=x
print(max)

#or 
print(list.sort())