#Module: A single Python file containing reusable code
def iseven(num):
    if num%2==0:
        return("even")
    else:
        return("odd")
    
def fact(num):
    f=1
    for k in range(1,num+1):
        f=f*k
    return(f)