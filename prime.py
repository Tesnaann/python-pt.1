#prime numbers are divisible only by 1 and that number itself
num1=int(input("Enter your number"))
if num1<=1:
    print("not a prime number")
for k in range(2,num1):
    if num1%k==0:
        print("not a prime number")
else:
    print("prime number")
 