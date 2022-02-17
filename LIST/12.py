# 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. 
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']

list1=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

del list1[5]
del list1[4]
del list1[0]
print(list1)