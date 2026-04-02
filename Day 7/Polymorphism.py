#Q.1)   WAP for Duck Typing: (Dynamic Typing)
#polymorphism example  
# class Principal:  
#     def role(self):  
#         print("i am managing all activity of college")  
  
# class Dean:  
#     def role(self):  
#         print('Dean= I am decision taking person')  
          
# class Hod:  
#     def role(self):  
#         print('Hod= I have responsibility of Teachers and Students')         
# class Faculty:  
#     def role(self):  
#         print('Faculty= I have to complete syllabus successfully')  
# # ========== class declaration completed=====================================  
# def  func(obj): # called func obj =1:Dean  
#     obj.role()# calling func  
# campus=[Principal(),Dean(),Hod(),Faculty()]   
# for obj in campus: #obj =[0:Principal(),1:Dean(),2:Hod()]  
#     func(obj)   # calling fun  

# Note:- The problem in this approach is if obj does not contain role() method then we will get AttributeError

#Method overloading
#Method name will have  same and argument will be difficult.
# Q.2)  WAP to understand why directly method overloading not supported in python.

# class Arithmatic:  
#     def add(self,a):  
#         print(a)  
#     def add(self,a,b):  
#         print(a+b)  
#     def add(self,a,b,c):  
#         print(a+b+c)  
# obj = Arithmatic()  
# obj.add(10)  #Error
# obj.add(10,20)  
# obj.add(1,2,3) 
# TypeError: Arithmatic.add() missing 2 required positional arguments: 'b' and 'c' 

# Q.3)  WAP to understand why directly constructor overloading not supported in python. Constructor overloading is not possible in Python If we define multiple constructors then the last constructor will be considered.

# class Arithmatic:  
#     def __init__(self):  
#         print("There is no argument")  
#     def __init__(self,a):  
#         print("passing one argument")  
#     def __init__(self,a,b):  
#         print("passing two arguments")  
  
# obj = Arithmatic()  
# obj = Arithmatic(10)  
# obj = Arithmatic(2,2) 
# TypeError: Arithmatic.__init__() missing 2 required positional arguments: 'a' and 'b'
 
# Method overriding-There has to be parent and child relationship.
# class Rbi:
#     def homeLoan_ROI(self):
#         print("Home Loan Rate of interest=7.5%")
#     def carLoan(self):
#         print("Car loan Rate of interest=8%")
# class Sbi (Rbi):
#     def homeLoan_ROI(self):
#         print("Home Loan Rate of interest=6.5%")
# obj = Sbi()
# obj.homeLoan_ROI()
# obj.carLoan()

#super
# class Rbi:
#     def homeLoan_ROI(self):
#         print("Home Loan Rate of interest=7.5%")
#     def carLoan(self):
#         print("Car loan Rate of interest=8%")
# class Sbi (Rbi):
#     def homeLoan_ROI(self):
#         print("Home Loan Rate of interest=6.5%")
#         super().homeLoan_ROI()
# obj = Sbi()
# obj.homeLoan_ROI()
# obj.carLoan()

# Q.5)  WAP to take the examples of constructor overriding. (Here when we create the object of child class that time child class constructor override the parent class constructor)

#Constructor overriding  
# class Father:  
#     def __init__(self):  
#         print("Father:= i am on time at breakfast table")  
  
# class Child(Father):  
#     def __init__(self):  
#         print("Child:= i will be late for breakfast")  
  
# obj = Child()  

#super()
# class Father:  
#     def __init__(self):  
#         print("Father:= i am on time at breakfast table")  
  
# class Child(Father):  
#     def __init__(self):  
#         print("Child:= i will be late for breakfast")  
#         super().__init__()
  
# obj = Child()  