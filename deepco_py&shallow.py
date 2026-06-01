#shalllow copy
import copy
a=[[1,2,3,4,5],[6,7,8,9,10]] #nested list
b=copy.copy(a) #shallow copy 
b[0][1]="python"  # [0][1]=2,first list,second element
print(a[0])
#output will be 1,"python",3,4,5 


# deep copy
import copy
c=[[1,2,3,4,5],[6,7,8,]]
d=copy.deepcopy(a)
d[0][1]="car"

print(a[0]) #no change in c


a=[[99,29,59,69,39],[33,66,44,55]]
print(a[0])  # output will be [99,29,59,69,39]
print(a[0][3]) # output will be 69

