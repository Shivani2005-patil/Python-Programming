#break() operation
# for i in range(1,5):
#     if i == 3:
#         break
#     print(i)

#continue() operation
# for i in range(1,5):
#     if i == 3:
#         continue
#     print(i)

# list=[10,20,30,40,50]
# for i in list:
#     print(i)

# mycart=[10,20,200,300,800,60,700]
# for i in mycart:
#     if i>400:
#         print("This my purchased cart item")
#         continue
#     print(i)

#WAP to calculate the sum of the list elements
# list=[1,2,3,4,5,6,7,8,9,10]
# sum=0
# for x in list:
#     sum=sum+x
#     print("The Sum=",sum)

# name="prashant"
# newname=""
# for i in name:
#     if i not in newname:
#         newname+=i
#     print(newname)
# for i in name:
#       newname+=i
#     print(i)

# rollno=[3,5,7,1,11,4,5,2]
# for x in rollno:
#     if x == 2 or x == 4 or x == 6 or x == 8 or x == 10:
#         print("even no is found ", x)
#         break

#s.replace(o;dstring,newstring)
#inside s, every occurance of oldstring will be replaced with newstring
# s=""
# s1=s.replace("difficult","easy")
# print(s1)
# #All occurances will be replaced
# s="ababababababab"
# s1=s.replace("a","b")
# print(s1)

# x=['A','B','C']
# y=['A','B','C']
# z=[1,2,3,4]
# print(x==y)
# print(x==z)
# print(x!=z)
# Is it comparing value or address

# val=[1,2,3,5,5,5,1,2,4,4,6,6,6]
# print(val.index(1))
# print(val.index(2))
# print(val.index(3))
# print(val.index(4))
# print(val.index(5))
# print(val.index(6))
#This index will return index number(position)

# n=[1,2,3,5,5,5,1,2,4,4,6,6,6]

# print(n.count(1))
# print(n.count(2))
# print(n.count(3))
# print(n.count(4))
# print(n.count(5))
# print(n.count(6))
# print(n.count(7))

# import datetime #datetime formatting
# date=datetime.datetime.now()
# print("It's now:{:%d/%m/%Y %H:%M:%S}".format(date))