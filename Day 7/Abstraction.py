# Q.1)  WAP to take the example of abstraction.

from abc import ABC, abstractmethod  
class Help4code(ABC): # abstract class  
    @abstractmethod # decorator  
    def training(self):# abstract method  
        pass  
       
    @abstractmethod   # abstract method  
    def placement(self):  
        pass  
  
class Ashish(Help4code):  
    def training(self):  
        print('C , C++ , Java')  
    def placement(self):  
        print("Java placement")  
  
class Ankush(Help4code):  
    def training(self):  
        print("Python | Django")  
    def placement(self):  
        print("Python placement students")  
  
class Prashant(Help4code):  
    def training(self):  
        print("Machine learning")  
    def placement(self):  
        print("Data science placement")  
  
obj1 = Ashish()  
obj1.training()  
obj1.placement()  
  
obj2 = Ankush()  
obj2.training()  
obj2.placement()  
  
obj3 = Prashant()  
obj3.training()  
obj3.placement()  


# Q.2) WAP for another example of abstract class.

# from abc import ABC, abstractmethod   
# class Irctc(ABC):#abstract class  
  
#     @abstractmethod  
#     def bookTicket(self): # abstract method  
#         pass  
  
# class MakeMyTrip(Irctc):  
  
#     def bookTicket(self):  
#         print( "  ==========================================")  
#         print("    Welcome To makemytrip   ")  
#         source      = input("Enter a source station name")  
#         destination = input("Enter destination name")  
#         date        = input("Enter date")  
#         print( "  ==========================================")  
          
# class GoIbibo(Irctc):  
      
#     def bookTicket(self):  
#         print("    Welcome To GOIBIBO")  
#         source      = input("Enter a source station name")  
#         destination = input("Enter destination name")  
#         date        = input("Enter date")  
  
# class Yatra(Irctc):  
      
#     def bookTicket(self):  
#         print("    Welcome To Yatra  ")  
#         source      = input("Enter a source station name")  
#         destination = input("Enter destination name")  
#         date        = input("Enter date")  
  
# m = MakeMyTrip()  
# m.bookTicket()  
# g = GoIbibo()  
# g.bookTicket()  
# y = Yatra()  
# y.bookTicket()  