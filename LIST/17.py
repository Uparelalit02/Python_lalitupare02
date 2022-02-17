# 17. Write a Python program to generate and print a list except for the first 5 elements, where the values are square of numbers between 1 and 30 (both included). 
list=[]
for i in range(1,31):
    c=i**2
    list.append(c)
print(list[5:])
