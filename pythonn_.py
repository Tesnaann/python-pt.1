#bubble sorting from user
'''size=int(input("Enter the size"))
a=[]
for k in range(size):
    l=int(input("Enter the number"))
    a=a+[l]
for i in range(size):
    for j in range(size-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)'''


#pallindrome
'''a=int(input("Enter the number"))
reversed_number=int(str(a)[::-1])
if a==reversed_number:
    print("Pallindrome")
else:
    print("Not pallindrome")'''

#sorting
size=int(input("Enter how many products you wish to enter"))
c={}
for k in range(size):
    name=input("Enter product name")
    price=int(input("Enter price of the product"))
    c[name]=price 
products=list(c.producta())


l=len(products)
for 



