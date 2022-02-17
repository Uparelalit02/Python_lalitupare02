# 66. Write a Python program to find the list in a list of lists whose sum of elements is the highest. 
# Sample lists: [1,2,3], [4,5,6], [10,11,12], [7,8,9]
# Expected Output: [10, 11, 12]
list1=[[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
print(max(list1, key=sum))

#OR

sum=[]
for i in list1:
    total=0
    
    
    for j in range(0,len(i)):
        total=total+i[j]
    sum.append(total)  

max=sum[0]

for x in sum:
    if max<x:
       max=x
for i in range(len(sum)):
    if max==sum[i]:
        print(list1[i])
