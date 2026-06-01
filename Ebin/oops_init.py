'''class Student:
    def __init__(self,n):
        self.name=n
    
    def display(self):
        print(self.name)

ob=Student("Tesna")
ob.display()'''

# Hierarchical inheritance 
class A:
    def __init__(self):
        self.a=10
        self.b=20
        self.c=30

class B(A):
    def display(self):
        self.bb=6
        print(self.a+self.b)    
class C(A):
    def display(self):
        print(self.b+self.c)

ob=B()
ob.display()
oc=C()
oc.display()


