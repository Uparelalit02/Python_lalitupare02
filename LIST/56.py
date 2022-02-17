# 56. Write a Python program to convert a string to a list. 
string1="lalit"
n=int(input("index: "))
list1=[string1]
print(list1)
list2=list(map(str,string1))
print(list2)
list2.remove(list2[n])
print(list2)