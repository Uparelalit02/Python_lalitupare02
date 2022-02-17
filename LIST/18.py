# 18. Write a Python program to generate all permutations of a list in Python. 

# listToStr = ''.join(map(str, list1))
# print(listToStr)
# for i in listToStr:
#     print(i)
    
# temp=list1.copy()
# k=0
# for i in range(0,2):
#
#     k=0
#     y=temp[k]
#     j=0
#     while j<3:
#         z=temp[j]
#         temp[j]=y
#         temp[k]=z
#         print(temp)
#         k=k+1
#
#         print(temp)
list1=[1,2,3]

for i in range(0,3):
    prev=0
    next=1

    while next<3:
        x=list1[prev]
        list1[prev]=list1[next]
        list1[next]=x
        prev=next
        next+=1
        print(list1)
    
    

