"""In an airport , the Airport  authority decides to charge some minimum amount to the passengers who are carrying luggage with them. They set a threshold weight value, say T, if the luggage exceeds the weight threshold you should pay double the base amount. If it is less than or equal to threshold then you have to pay $1. """
def weight_count(N,weights,T):
    value=0
    for i in weights:
        value+=1
        if i>T:
            value+=1
    return value
N=int(input("No of luggeges"))
weights=[]
for i in range(N):
    weights.append(int(input("enter weights")))
T=int(input(":"))
res=weight_count(N,weights,T) 
print(res)          