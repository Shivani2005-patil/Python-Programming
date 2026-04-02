class Student:  
    # by using class name we can access static method  
    @staticmethod # decorator  
    def get_personal_detail(firstname,lastname):  
        print("your personal detail=",firstname,lastname)  
  
    @staticmethod  
    def contact_detail(mobil_no, rollno):  
        print("your contact detail=", mobil_no,rollno)  
  
Student.get_personal_detail("prashant", "jha")  
Student.contact_detail(5456454646, 1001) 