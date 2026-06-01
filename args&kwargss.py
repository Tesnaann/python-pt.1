#args collects multiple positional arguments into a tuple 
#**kwargs collects keyword arguments into a dictionary.

#args
def nums(*args):
    print(args)

nums(12,4,6)
nums(19,3)

def greeting(**kwargs):
    print(kwargs) 

greeting(name="Tesna",age=19)
greeting(name="Tesna",age=19,place="Kochi")

def add (*args):
    print(args)
add(2,4,5)
def add(**kwargs):
    print(kwargs)
add(name="Tesna",age=19)
