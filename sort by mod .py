def mysort(x):
   return x%7
mylist=[2,3,4,14,7]
mylist.sort(key=mysort)
print(mylist)
