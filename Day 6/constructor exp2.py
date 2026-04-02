class Hod:   
    def __init__(self):# constructor  
        self.name='prashant jha'   
        self.age=53             
        self.empid=1001          
    def info(self):# instance method  
        print("My name is :",self.name)  
        print("My Age is:",self.age)   
        print("My emp id:",self.empid)    
  
obj = Hod()#object create  
obj.info()  