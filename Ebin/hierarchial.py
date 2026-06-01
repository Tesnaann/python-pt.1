# Hierarchical inheritance -multiple child classes inherit from same parent class
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
