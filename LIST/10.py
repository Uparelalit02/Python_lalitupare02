# 10. Write a Python program to find the list of words that are longer than n from a given list of words. 
list=['abc0','bsjf','sdfhwui']
n=4
c=[]
for i in list:
    if len(i)>n:
        c.append(i)
print(c)