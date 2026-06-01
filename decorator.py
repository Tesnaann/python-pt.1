#A decorator is essentially a function that takes another function as an argument
'''def mydecorator(fun): #fun -->add
    def wrapper (a,b):
        if a>0 and b>0:
            fun(a,b) #fun(1,3)--> add(1,3)
        else:
            print("Numbers should be greater than 0")
    return wrapper

def add(a,b):
    print(a+b)

myfun=mydecorator(add) #--> wrapper
myfun(1,3)    #wrapper(1,3)'''




def mydecorator(fun): #fun -->add
    def wrapper (a,b):
        if a>0 and b>0:
            fun(a,b) #fun(1,3)--> add(1,3)
        else:
            print("Numbers should be greater than 0")
    return wrapper

@mydecorator
def add(a,b):
    print(a+b)
add(2,6)



def mydecorator(fun):
    def wrapper(a,b):
        if a>0 and b>0:
            fun(a,b)
        else:
            print("should be greater than one")
    return wrapper

@mydecorator
def sub (a,b):
    print(a-b)
sub(5,3)