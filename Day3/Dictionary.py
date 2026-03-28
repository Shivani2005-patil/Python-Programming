#WAP for implementing dictionary and its function:
#Example 1: Take input as key-value pair and display output  
# mydict = {  
#   "name": "prashant",  
#   "professional": "developer",  
#   "empid": 1001   
# }  
# print(mydict)  
# print(type(mydict)) 

# Example 2: Take input as key and display the value  
# mydict = {  
#   101: "prashant",  
#   102: "ashish",  
#   "103": "mohini",  
#   "104": "trivani",  
#   101: "ashish",  
#   104: "ashish"  
# }   
# print(mydict)  
# With the help of key we have to print values.
# a = mydict[102]  
# print(a)  

# Example 3: Change values with the help of keys
# we will replace old value by new value.  
# mydict[102] = "peter"  
# print(mydict)  

# Example 4: Print only keys using a loop
# only print key x=0,1   
# for x in mydict:  
#      print(x)  

# Example 5: Print only values using values() function 
#only print values x=0
# for x in mydict.values():  
#      print(x)  

# Example 6: Print keys and values using items() function  
# for x, y in mydict.items():  
#     print(x, y) 

# Example 7: Add a new key-value pair  
# mydict["mobile_no"] = 4646463738  
# print(mydict) 

# Example 8: Remove key-value pair using pop() function  
# pop() method will remove pair by specific key name.
# mydict = {  
#   101: "prashant",  
#   "professional": "developer",  
#   "empid": 1001 
# }
# mydict.pop(101)  
# print(mydict)  

# Example 9: Create a clone of the dictionary  
# newdict = mydict.copy()  
# print(newdict)  