#find how many upparcase and lowercase digits and latters in string
def count(str):
    upper,lower,number,special=0,0,0,0
    for i in range(len(str)):
        if str[i].isupper():
            upper +=1
        elif str[i].islower():
            lower +=1
        elif str[i].isdigit():
            number +=1
        else :
            special +=1
    print("upper",upper)
    print("lower",lower)
    print("number",number)
    print("special ",special)
str="HekkiHeiae"
count(str)                        