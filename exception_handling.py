'''a="100"
b=10
try:
    result=a/b  #string dev by int
except ArithmeticError:
    print("Arithmetic problem")
except:
    print("something went wrong")'''




a=[1,23,5]
try:
    print(a[1])
except NameError:
    print("Name is not defined")
except TypeError:
    print("provide correct values")
except IndexError:
    print("index position not found")
except Exception as e: # to print what is the eroor, 'e' is just a varibale
    print("error",e)
else:
    print("executed in try block") # this will for if thr progrm work in the try block itself
finally: # this will work for both try as well as except 
    print("completed")



