'''x=10
def show():
    x=5
    print(x) #output5
show()
print(x) # global is not used here so when printin is outside the fn output will be 10 and 
 #output10        # if printing is done inside the fn output will be 5
'''
'''x=10    
def add():
    global x
    x=5
    print(x)  #output5
add()
print(x)      #output5

x=10
def add():
    global x
    x=x+5
add()
print(x) #output15'''
