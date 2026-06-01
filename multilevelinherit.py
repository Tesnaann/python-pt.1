#child inherits from a parent class and then another class (derived) inherits from that child class, forming a chain 
#multilevel
class grandparents:
    def fun1 (self):
        print("I am the grand parents")
class parents(grandparents):
    def fun2 (self):
        print("I am the parents")
class child(parents):
    def fun3(self):
        print("I am the child")
o=child()
o.fun1()
o.fun2()
o.fun3()

class a:
    def method1(self):
        self.a=10
class b(a):
    def method2(self):
        self.b=20
class c(b):
    def method3(self):
        print(self.a+self.b)
obj=c()
obj.method1()
obj.method2()
obj.method3()







#using keyword super(),multilevel
class A:
    def __init__(self):
        self.a=10
class B(A):
    def __init__(self):
        super().__init__() # here only B work, so super is used
        self.b=20
class C(B):
    def add (self):
        print(self.a+self.b)
oc=C()
oc.add()
        

