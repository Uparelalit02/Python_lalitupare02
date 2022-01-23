'''a string which is a mix of letter and integer and special char from which find the number from avalable digit after removing duplicates
if addiion of numbers is not even number return -1
ex:infosys@334
OP:-1'''
input =input("enter")
s=set()
for i in input:
  if i.isdigit():
    s.add(int(i))
sum=0
for i in s:
  sum=sum+i
if sum%2==0:
  print("1")
else:
  print("-1")    
      