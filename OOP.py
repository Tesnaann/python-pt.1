#object oriented programming


class Student: # class is a keyword used to create class and student is class name,first letter in caps
    institute="one team" #class variable
    def setDetails(self,n,a):#self is a reference to the current object(instance)of a class.
        self.name=n
        self.age=a
    def greet(self):
        print(f"Hello {self.name},you are {self.age} years old")
std1=Student() #std1 is object name which should be unique
std2=Student()
std1.setDetails("Ebin",27)
std2.setDetails("Tesna",19)

std1.greet()
std2.greet()


class Student:
    institute="One team"
    def __init__(self,n,a): #__init__ is a built in method 
        self.name=n
        self.age=a

    def greetings(self):
        print(f"Hello, {self.name},You are{self.age}years old")
    
std1=Student("Ebin",27)
std2=Student("Tesna",19)

std1.greetings()
std2.greetings()
              



