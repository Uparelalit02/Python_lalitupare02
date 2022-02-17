# 11. Write a Python function that takes two lists and returns True if they have at least one common member. 
list12=[2,3,6,5,8]
list22=[2,3,5,4,8]
def sim(list1,list2):
    for i in list1:
        for j in list1:
            if i==j:
                c=" true"
            else:
                c="false"
    return c
print(sim(list12,list22))