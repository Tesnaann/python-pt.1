def add (x,y):
    return(x+y)
a=int(input("Enter first number"))
b=int(input("Enter second number"))
print("sum=",add(a,b))


def fact(nums):
    f=1
    for k in range (1,nums+1):
        f=f*k
    return f
a=int(input("Enter your number"))
print("fact=",fact(a))

