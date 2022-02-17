# 30. Write a Python program to get the frequency of the elements in a list. 
list=[1,1,1,2,3,4,4,4,4,7,7,8,9]
fre={}
for i in list:
    if i in fre:
        fre[i]+=1
    else:
        fre[i]=1
print(fre)