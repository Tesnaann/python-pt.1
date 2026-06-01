# Getting size of list 
size=int(input("Enter your size"))
numbers=[]
# Getting each input number from  user and storing it in numbers list 
for g in range(size):
    num=int(input("Enter the number"))
    numbers=[num]+numbers
print("Prime numbers are : ",end="")
# Looping numbers list and checking each number whether it is prime or not
for n in numbers:
    if n<=1:
        print("not a prime number")
    for k in range(2,(n//2)+1):
        if n%k==0:
            break
    else:
        print(n,end=" ")


