# 45. Write a Python program to convert a pair of values into a sorted unique array. 
n=[(1,2),(2,3),(3,4),(1,4),(5,2)]
# print(n)
# print(sorted(set().union(*n)))
# #OR 

list1=[(1,2),(2,3),(3,4),(1,4),(5,2)]
for i in range(0,len(list1)-1):
    for j in  range(0,len(list1)-1):
        if list1[j][1]>list1[j+1][1]:
                t=list1[j]
                list1[j]=list1[j+1]
                list1[j+1]=t

print(list1)

for i in range(0,len(list1)-1):
    for j in  range(0,len(list1)-1):
        if list1[j][0]>list1[j+1][0]:
                t=list1[j]
                list1[j]=list1[j+1]
                list1[j+1]=t

print(list1)
        
        