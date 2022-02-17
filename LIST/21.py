# 21. Write a Python program to convert a list of characters into a string. 
list=['a','b','c','d']
string="".join(map(str,list))
print(string)

#or 
def listToString(s): 
    str1 = "" 
    for ele in s: 
        str1 += ele  
    return str1 

print(listToString(list))