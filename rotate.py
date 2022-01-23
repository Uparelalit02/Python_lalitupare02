string=input()
num=input()
def rotate(st,n):
    n=list(str(n))
    s=0
    print(n)
    for i in n:
        s+=int(i)**2
    if s%2==0:
        return st[-1:]+st[:len(st)-1]
    else:
        return st[2:]+st[:2]
res=rotate(string,num)