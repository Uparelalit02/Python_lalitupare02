# n=input("enter number")

# first=int(n[0])
# last=int(n[-1])
# add=first+last
# print(add)
n = int(input("enter a number"))
n1 =  n % 10
sum = 0
while n > 10:
    n = n // 10
sum = n1 + n
print( sum )