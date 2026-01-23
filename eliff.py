num1=int(input("Enter your first no:"))
num2=int(input("Enter your sec no:"))
print("1:Addition")
print("2:substraction")
print("3:Division")
print("4:multiplication")
choice=int(input("Enter your choice"))
if choice==1:
    print(num1+num2)
elif choice==2:
    print(num1-num2)
elif choice==3:
    print(num1/num2)
elif choice==4:
    print(num1*num2)
else:
    print("invalid choice")