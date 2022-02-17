# 32. Write a Python program to check whether a list contains a sublist. 
list1=[1,2,3,4,5,6,7,8,9]
list2=[5,6,7]
s1="".join(map(str,list1))
s2="".join(map(str,list2))
print(s1,s2)

#or
if (s1.find(s2)==-1):
    print("no")
else:
    print("yes")
