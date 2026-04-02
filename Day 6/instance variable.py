class New:
    def __init__(self):
        self.a = 10
        
Obj1 = New()
Obj2 = New()
Obj3 = New()
print(Obj1.a)
print(Obj2.a)
print(Obj3.a)
Obj1.a = 20
print(Obj1.a)
print(Obj2.a)
print(Obj3.a)

    