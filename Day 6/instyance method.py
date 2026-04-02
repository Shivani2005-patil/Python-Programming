class Student:  
    def __init__(self, name, rollno, mob):  
        self.name= name    # instance variable  
        self.rollno= rollno  
        self.mob = mob  
  
    def display(self): # instance method  
        print(self.name," ",self.rollno, " ",self.mob)  
  
stud = Student("prashant", 1001, 6464646464)  
stud.display()