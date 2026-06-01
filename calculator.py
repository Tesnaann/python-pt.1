while True:
    num1=int(input("Enter first number"))
    num2=int(input("Enter second number"))
    print("1:Addition")
    print("2:Substraction")
    print("3:Multiplication")
    print("4:division")
    choice=int(input("Enter your choice:"))
    if choice==1:
        print(num1+num2)
    elif choice==2:
        print(num1-num2)
    elif choice==3:
        print(num1*num2)
    else:
        print(num1/num2)
    s=input("Do you wish to continue (Y/N)")
    if s!="Y":
        break
    
 


