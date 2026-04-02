class New:
    a= 10
    def __init__(self):
        self.name="prashant" 
        
Obj1 = New()
Obj2 = New()
Obj3 = New()
print(Obj1.a)
print(Obj2.a)
print(Obj3.a)
New.a = 50
print(Obj1.a)
print(Obj2.a)
print(Obj3.a)

