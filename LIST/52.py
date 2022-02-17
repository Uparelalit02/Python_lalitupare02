# 52. Write a Python program to compute the similarity between two lists. 
# Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]
# Expected Output: 
# Color1-Color2: ['white', 'orange', 'red']
# Color2-Color1: ['black', 'yellow']


color1=["red", "orange", "green", "blue", "white"]
color2=["black", "yellow", "green", "blue"]
ans=[]
ans1=[]
for i in color1:
    if i not in color2:
        ans.append(i)
print("Color1-Color2: ",ans)

for j in color2:
    if j not in color1:
        ans1.append(j)
print("Color2-Color1: ",ans1)

