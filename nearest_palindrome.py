


def near_pali(n):
    while True:
        rev=str(n)[::-1]
        if rev==n:
            return int(n)
            break 
        else:
            n =n+1
n=int(input(":"))
result=near_pali(n)                
print(result)