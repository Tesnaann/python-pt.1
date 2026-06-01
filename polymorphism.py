#polymorphism in operators.
print(5+10)#integer addition
print("Hello"+"world") #string concatenation


#polymorphism in  functions
class Pen:
    def use(self):
        return "Writing"

class Eraser:
    def use(self):
        return "Erasing"

print(Pen().use())
print(Eraser().use())


#polymorphism in built in functions
print(len("Hello"))# length of string
print(len([1,2,3,4])) #list length

print(max(1,3,5))# max of int
print(max("a","z","n"))
