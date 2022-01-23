# num=int(input())#195
# sum=0
# while True:
#     sum=num+int(str(num)[::-1])
#     if str(sum)==str(sum)[::-1]:
#         print(sum)
#         break
#     else:
#         num=sum

# N=int(input("Enter value of N:"))
# people=[]#4,2,7
# house=[]#-1,-1,-1
# for i in range(N):
#     people.append(int(input()))
# for i in range(N):
#     house.append(int(input()))
# count=0
# for i in range(N):
#     for j in range(N):
#         if (people[i]<house[j]):
#             count+=1
#             house[j]=-1
#             break
# print(N-count)



#Second day



'''find repeated strings count and print that string by using set'''

# s="cat batman latt matter cat matter cat"
# list=s.split()
# # print(list)
# count=0
# s1=set()
# for i in range(0,len(list)):
#     x=list[i]
#     for j in range(0,len(list)):
#         if list[j]==x:
#             count=count+1
#     if count>1:
#         s1.add(x)
#     count=0
# print(s1)


'''write a program to remove duplicates'''
# l=[10,10,20,30,20,40,50,60,50]    # output: [10,20,30,40,50,60]
# lst=[]
# for i in l:
#     if i not in lst:
#         lst.append(i)
# print(lst)


'''1.WAP to find no of occurance of each letter present in the given string'''

#output= {'a': 3, 'b': 2, 'c': 1}


# s="vyankatesh"
# list=['a','e','i','o','u']
# dict={} # empty dictionary
# x=''
# count=0
# vowels=0
# for i in s:
#     if i in list:
#         vowels=vowels+1
#     x=i
#     for j in s:
#         if x==j:
#             count=count+1
#     dict[x]=count
#     count=0
# print(dict)
# print(vowels)







'''2.find count of string from string'''
# s="timabcdtimdjfksnfoitim"
# a="tim"
# res=s.count(a)
# print(res)





#
# '''3.length of given interger'''
# # 101==> Output=3
#
# #
# def num_len(num):
#     count=0
#     while num>0:
#         num=num//10
#         count+=1
#     return count
#
# result=num_len(101)
# print(result)






'''5.find the strong number(Strong number is a special number whose sum of the factorial of 
digits is equal to the original number. )    145== 1!+4!+5!== 145'''
# Input=145

# def strong_num(num):
#     sum=0
#     fact=1
#     temp=num #temp=145
#     while num>0:
#         rem=num%10 #rem=5
#         num=num//10 #num=14
#         for i in range(1,rem+1):
#             fact=fact*i
#         sum=sum+fact
#         fact=1
#     if sum==temp:
#         print("This is strong no",sum)
#     else:
#         print("This is not strong NO",sum)
# strong_num(456)

















#prime no:

# num=int(input())
# for i in range(2,num):
#     if num%i==0:
#         print("it is not prime no")
#         break
# else:
#     print("prime no")




# Fibonacci series

# num=int(input())
# n1=0
# n2=1
# n3=0
# i=0
# if num==0:
#     print("not valid number")
# elif num==1:
#     print(n1)
# else:
#     while i<num:
#         print(n1,end=" ")
#         n3=n1+n2
#         n1=n2
#         n2=n3
#         i+=1





#GCD / HCF


# def getgcd(a,b):
#     if a>b:
#         small=b#20
#     else:
#         small=a
#     for i in range(1,small+1):# 1 to 20
#         if ((a%i==0) and (b%i==0)):#20%1
#             gcd=i
#     return gcd
#
# result=getgcd(20,60)
# print(result)




#pattern
'''* * * *
   * * * *
   * * * *
   * * * *'''
#
# for x in range(1,5):
#     for y in range(1,5):
#         print("*", end=" ")
#     print()


'''
*
* *
* * *
* * * *'''

# for x in range(1,5):
#     for y in range(1,x+1):
#         print("*", end=" ")
#     print()

'''
A
B B
C C C
D D D D
E E E E E
'''

# for x in range(65,70):
#     for y in range(65,x+1):
#         print(chr(x),end=" ")
#     print()
'''
A
A B
A B C 
A B C D
A B C D E
'''
# for x in range(65,70):
#     for y in range(65,x+1):
#         print(chr(y),end=" ")
#     print()

'''
    *
   **
  ***
 ****
***** 
'''
# for x in range(1,6):
#     for y in range(5,x,-1):
#         print(" ",end=" ")
#     for z in range(0,x):
#         print("*",end=" ")
#     print()


# for i in range(6,1,-1):
#     print(i)

'''
    *
   * *
  * * *
 * * * *
* * * * *
'''

# for x in range(1,6):
#     for y in range(5,x,-1):
#         print(" ",end="")
#     for z in range(0,x):
#         print("*",end=" ")
#     print()

'''
*
* *
* * *
* * * *
* * *
* *
*
'''
#
# size=3
# for x in range(size,-(size+1),-1):
#     for y in range(size,abs(x)-1,-1):
#         print("*",end=" ")
#     print()


"a4b3c2 ======>  aaaabbbcc"
#
# s="a4b3c2"
# t=""
# for i in s:
#     if i.isalpha():
#         x=i
#     else:
#         d=int(i)
#         t=t+x*d
# print(t)


'''Find how many uppercase and lowercase characters and digits and letters in a string  '''
#input=DJKsdkjn4979
#
# def count_all(s):
#     letter=0
#     digit=0
#     lowercase=0
#     uppercase=0
#     for i in s:
#         if i .isalpha():
#             letter+=1
#         if i.isnumeric():
#             digit+=1
#         if i.islower():
#             lowercase+=1
#         if i.isupper():
#             uppercase+=1
#     print("letter:",letter)
#     print("digit: ",digit)
#     print("lowercase: ", lowercase)
#     print("uppercase",uppercase)
#
# count_all("DJKsdkjn4979")






'''A string which is a mixture of letter and integer and special char 
from which find the  number from the available digit 
after removing the duplicates.
If an adition of numbers is not even number  return-1.
Ex: infosys@334
O/p:-1'''

# input=input(": ")
# s=set() #empty set
#
# for i in input:
#     if i.isdigit():
#         s.add(int(i))
# sum=0
# for i in s:
#     sum=sum+i
# if sum%2==0:
#     print("1")
# else:
#     print("-1")





#REVERSE STRING without slice and reversed:

# s="ABCD"
# #output=DCBA
#
# s1=""
# for i in s:
#     s1=i+s1
# print(s1)



'''Write a python function nearest_palindrome ()
Which can accepts a number and return the nearest greater palindrome number.
Input: 12300 -> output: 12321
Input: 12331 -> output: 12421'''
#
# def nearest_palindrome (n):
#     while True:
#         rev=int(str(n)[::-1])
#         if rev==n:
#             return int(n)
#             break
#         else:
#             n+=1
#
#
# n=int(input(": "))
# result=nearest_palindrome(n)
# print(result)






'''Nearest prime number: '''
#input=24
#ouput=29

# def nearest_primeno(n):
#     while True:
#         for i in range(2,n):
#             if n%i==0:
#                 n=n+1
#                 break
#         else:
#             return n
#             break
#
# n=int(input(":"))
# res=nearest_primeno(n)
# print(res)



'''For a given list of numbers find the its factors and add the factors then if the sum of 
all factor is present in original list and print it
Ex:
Input: 0,1,6
Factors: 0 = 0, sum =0
1 = 1, sum =1
6 =1,2,3 = sum =6
Output:0,1,6
If the sum is not present in the list then return -1.'''


# def factor(n):
#     s=0
#     if n==1:
#         return 1
#     for i in range(1,n):
#         if n%i==0:
#             s+=i
#     return s
#
# list1=list(map(int,input().split(",")))
# flag=0
# for i in list1:
#     if factor(i) in list1:
#         flag=1
#         print(i)
#
# if flag==0:
#     print("-1")




# #0,1,6
# list1=list(map(int,input().split(",")))
#
# print(list1)















# WAP taking alternative string , for same length of string

# s1="RAVI"
# s2="TEJA"
# #output=R T A E V J I A
#
# s3=[]
# for i in range(0,len(s1)):
#     s3.append(s1[i])
#     if i>len(s2):
#         break
#     else:
#         for j in range(i,i+1):
#             s3.append(s2[j])
#
# print(s3)
# s4="".join(s3)
# print(s4)















# def weight_count(N,weights,T):# weights==1,2,3,4   T=3
#     value=0# 5
#     for i in weights:
#         value+=1
#         if i>T:
#             value+=1
#     return value
#
# N=int(input(" : "))
# weights=[] #empty list 1,2,3,4
# for i in range(N):
#     weights.append(int(input()))
# T=int(input(": " ))
#
# res=weight_count(N,weights,T)
# print(res)








'''13. String rotation

Input rhdt:246, ghftd:1246
Expl: here every string is associated with the number sep by : 
if sum of squares of digits is even then rotate the string by 1 if square of digits
is odd then rotate the string left by 2 position. 2*2+4*4+6*6=56 which is even so rotate rhdt ->trhd 
1*1+2*2+4*4+6*6=57 which is odd then rotate string by 2 at left ‘ghftd --> hftdg--> ftdgh”
o/p: ftdgh'''

# s=input().split(",")
# strings=[]
# nums=[]
# for i in s:
#     s1,n=i.split(":")
#     strings.append(s1)
#     nums.append(n)
# def rotate(st,n):#rhdt --> trhd
#     n=list(str(n))
#     s=0
#     print(n)
#     for i in n:
#         s+=int(i)**2
#     if s%2==0:
#         return st[-1:]+st[:len(st)-1]
#     else:
#         return st[2:]+st[:2]
#
# for i in range(len(nums)):
#     print(rotate(strings[i],nums[i]))





