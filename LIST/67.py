# 67. Write a Python program to find all the values in a list are greater than a specified number. 
list1=[23,24,32,43]
num=12

def num_grater(list1):
    for i in list1:
        if i>num:
            c="All num are greater than given num"
        else:
            c="none"
        return c
print(num_grater(list1))