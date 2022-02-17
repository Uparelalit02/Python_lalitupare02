# 35. Write a Python program to create a list by concatenating a given list which range goes from 1 to n. 
# Sample list : ['p', 'q']
# n =5
# Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']

from re import X


list=['p','q']
n=5
new_list=['{}{}'.format(x,y) for y in range(1,n+1) for x in list]
print(new_list)

#OR

l1=[]
for y in range(1,n+1):
    for x in list:
        c=x+str(y)
        l1.append(c)


print(l1)
