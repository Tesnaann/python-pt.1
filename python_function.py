#keyword,function name,parameter
def greetings(name):# function definition
    print("Hello",name)

greetings("Tesna") #function call
greetings("Ebin")

def oddeven(number):
    if number%2==0:
        print("Even") 
    else:
        print("odd")
oddeven(26) 
oddeven(33)


def total(nums):
    total=0
    for k in nums:
        total=total+k
    return total
    
l=[12,13,14,15]
s=total(l)
print(s/len(l)) #or print(total(l)/len(l))



        
        

    


