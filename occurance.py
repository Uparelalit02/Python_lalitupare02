#find no of occurance of each letter present in given string
s="aaabbc"
dict={} #empty dict
x=''
count=0
for i in s:
  x=i
  for j in s:
    if x==j:
      count=count+1
  dict[x]=count
  count=0
print(dict)     