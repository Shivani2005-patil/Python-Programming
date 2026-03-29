#while syntax:
# initilalization
# while condition:
#      #Statement
#      #inc/dec

#Basic Examples.
# i=1 
# while i<=5:
#     print(i)
#     i=i+1
#WAP to print sum of natural number from 1 to 10 using while loop 1+2+3+4+5+6+7+8+9+10=55
# sum=0
# i=1
# while i<=10:
#     sum=sum+i
#     i=i+1
# print("Sum",sum)

#WAP to print the count of even and odd from 1 to 10 using while loop
# even=0
# odd=0
# i=1                                 
# while i<=10:
#     if i%2 ==  0:
#         even = even+1
#     else:
#         odd = odd+1
#     i = i+1
# print("Even=",even)
# print("Odd=",odd)

#zip()
# for i,j in zip(range(1,6), range(5,0,-1)):
#     if i==3 and j==3:
#         continue
#     print(i," ",j)

#WAP using while loop 5*4*3*2*1=120
# fact=1
# i=5
# while i>0:
#     print(i, end="")
#     fact=fact*i
#     i= i-1
#     if i>0:
#         print("*", end="")

# print("= ",fact)

#WAP using while loop fibonacci series 
# n=10
# a=0
# b=1
# count=0
# while count<n:
#     print(a, end=" ")
#     c=a+b
#     a=b
#     b=c
#     count=count+1

# username=" "
# password=0
# while username!="admin" or password!= 12345:
#      username=input("Enter username :")
#      password=int(input("Enter password :"))