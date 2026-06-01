#qn 1
for k in range(1,5):
    for j in range(k,0,-1):
        print(j,end="")
    print()'''
#2 to 40 even nos using list comprehension
'''a=[x for x in range(2,41)if x%2==0]
print(a)
#3 fct using fn
def fact(num):
    if num<1:
        print("not prime number")
    elif num==1:
        print("prime number")
    for k in range(2,num+1):
        if num%k==0:
            print("not prime")
            break
        else:
            print("prime number")
fact(1)


a=[]
size=int(input("enter size"))
for k in range(size):
    b=int(input("Enter number"))
    a=a+[b]
for i in range(size):
    for j in range(size-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)






