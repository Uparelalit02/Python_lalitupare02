# 68. Write a Python program to extend a list without append. 
# Sample data: [10, 20, 30]
# [40, 50, 60]
# Expected output : [40, 50, 60, 10, 20, 30]

list1= [10, 20, 30]
list2=[40, 50, 60]
list3="".join(list(map(str,list1)))
list4="".join(list(map(str,list2)))
print(list3,list4)
list4=list3+list4
print(list4)


#OR

list1[:0]=list2
print(list1)