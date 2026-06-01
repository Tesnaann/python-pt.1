#armstrong number
num=int(input("Enter your number"))
n=num
power=len(str(num))
total=0

while n>0:
 digit=n%10 # 153%10=3
 total=total+digit**power #** floor div which gives power
 n//10 #remove last digit of n

 if total==num:
  print("Armstrong no")
else:
 print("not armstrong no")
