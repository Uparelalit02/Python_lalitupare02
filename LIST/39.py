# 39. Write a Python program to convert a list of multiple integers into a single integer. 
# Sample list: [11, 33, 50]
# Expected Output: 113350

list=[11,22,50]
list2="".join(map(str,list))
print(list2)