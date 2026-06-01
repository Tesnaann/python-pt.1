#diamond pattern
n=5
for i in range(1,n+1):
    print(" "*(n-i) + "*"*(2*i-1))  #top part of diamond,odd number of stars (1,3,5,7…)

for i in range(n-1,0,-1):
    print(" "*(n-i) + "*"*(2*i-1))



#To find area of a cirlce
import math
class circle:
    def __init__ (self,radius):
        self.radius=radius
    def area(self):
        return math.pi*self.radius**2  #area = pi r2
    def perimeter(self):
        return 2*math.pi*self.radius #pperimeter is 2pir
c=circle(5)
print("Area",c.area())
print("Perimeter=",c.perimeter())


#rectangle
class rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
    def perimeter(self):
        return 2*(self.length+self.width)
r=rectangle(6,4)
print("Area=",r.area())
print("Perimeter",r.perimeter())

    
