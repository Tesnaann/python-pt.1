#single inheritance-one parent and one child
class Animals: # parent class
    def __init__(self,name):
        self.name=name

    def info (self):
        print("Animal name",self.name)

class dog(Animals):  
    def breeds(self,b):
        self.breeds=b
    def displaybreed(self):
        print("Breed:",self.breeds)

    def sound(self):
        print(self.name,"bark")
d=dog("buddy")
d.breeds("lab")
d.displaybreed()
d.info()
d.sound()

#multiple
class A:
    def __init__(self):
        print("Hello methoda")
        B.__init__(self) #only A will work if this is not written .ie,output=hello methoda
class B:
    def __init__(self):
        print("Hello methodb")
class C(A,B): #A will work first and then B here
    pass
oc=C()



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

        


