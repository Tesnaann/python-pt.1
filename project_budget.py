import re
import copy
expense_count=0 #global variable

def logger(func): # decorator
    def wrapper(*args,**kwargs):
        print("\n Function Started")
        result=func(*args,**kwargs)
        print("---function finished---")
        return result
    return wrapper


class Expense:
    organizer_name="Personal expense organizer"
    def __init__(self,item,category,amount,email):
        self.item=item
        self.category=category
        self.amount=amount
        self.email=email

def display(self):
    print(f"Item:{self.item}| category:{self.category}|Amount:{self.amount}|email:{self.email}")

def expense_level(self):
    if self.amount>1000:
        return "high expense"
    elif self.amount>500:
        return "medium expense"
    else:
        return "low expense"

@classmethod
def change_name(cls,new_name):
    cls.organizer_name=new_name
@staticmethod
def check_amount(amount):
    return amount >=0

def validate_email(email):
    pattern=r'[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern,email)
def bubble_sort(data,key=lambda x:x):
    arr=data.copy()
    n=len(arr)

    for i in range(n):
        for j in range(0,n-i-1):
            if key(arr[j])>key(arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

@logger
def create_expenses(*args,**kwargs):
    expenses=[]

    for e in args:
        expenses.append(e)
    for key,value in kwargs.items():
        print(key,value)
    return expenses
def save_expenses(expenses):
    try:
        with open("expenses.txt","w") as file:
            for e in expenses:
                file.write(f"{e.item},{e.category},{e.amount},{e.email}\n")
        print("expenses saved to file")
    except Exception as e:
        print("File error",e)
def load_expenses():
    expenses=[]
    try:
        with open("expenses.txt","r") as file:
            for line in file:
                line=line.strip()
                if not line:continue
                parts=line.split(",")
                if len(parts)==4:
                 item,category,amount,email=parts 
                 expenses.append(Expense(item,category,int(amount),email))
    except FileNotFoundError:
        print("No previous expense file found")
    return expenses
def menu():
    print("\n===== PERSONAL EXPENSE ORGANIZER=====")
    print("1.Add expense")
    print("2.view expense")
    print("3.sort by amount")
    print("4.zip example")
    print("5.exit")

def main():
    global expense_count
    expenses=load_expenses()

    while True:
        menu()

        try:
            choice=int(input("Enter choice:"))
        except ValueError:
            print("Invalid input")
            continue
        match choice:
            case 1:
                item=input("Enter item name:")
                category=input("Enter category:")
                email=input("Enter email")
                
                if not validate_email(email):
                   print("Invalid email")
                   continue
                amount=int(input("Enter amount"))
                if not Expense.check_amount(amount):
                    print("invalid amount")
                    continue
                e=Expense(item,category,amount,email)
                expenses.append(e)
                expense_count +=1
                print("Expenses added successfully")
            case 2:
                for e in expenses:
                    e.display()
                    print("Level:",e.expense_level())
            case 3:
                sorted_expenses=bubble_sort(expenses,key=lambda x:x.amount)
                print("\n Sorted Expenses")
                for e in sorted_expenses:
                   print(e.item,e.amount)

            case 4:
               items=[e.item for e in expenses]
               amounts=[e.amount for e in expenses]
               print("\nZip Result")
               for i,a in zip(items,amounts):
                print(f"{i}:{a}")       
            case 5:
             break
#copies
             shallow_copy=expenses.copy()
             deep_copy=copy.deepcopy(expenses)

             print("\n shallow copy length:",len(shallow_copy))
             print("Deep copy length:",len(deep_copy))
             save_expenses(expenses)
             print("exiting")
if __name__=="__main__":
    main()

                
        
