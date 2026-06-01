#Lambdas are small, short-lived functions created and used immediately, 
# mainly to pass simple logic as an argument to another function.
a=lambda x,y:(x+y,x*y,x-y)
result=a(5,10)
print(result)

a=lambda x: "Even" if x%2==0 else "odd"
result=a(5)
print(result)
