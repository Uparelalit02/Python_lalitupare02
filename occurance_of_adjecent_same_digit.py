# #lex_auth_012693750719488000124
# Given a list of integer values. Write a python program to check whether it contains same number in adjacent position. Display the count of such adjacent occurrences

# Sample Input

# Expected Output

# [1,1,5,100,-20,-20,6,0,0]

# 3

# [10,20,30,40,30,20]

# 0

# [1,2,2,3,4,4,4,10]

# 3
def get_count(num_list):
    count=0

    for i in range(len(num_list)-1): #Because you have alist[i+1] in for loop , you cant go through list until end , so you have to end it one element before end:
        if(num_list[i]==num_list[i+1]):
            count=count+1
        

    return count

#provide different values in list and test your program
num_list=[1,1,5,100,-20,-20,6,0,0]
print(get_count(num_list))