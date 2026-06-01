'''a=[1,2,3,4,2,3,5]
newlist=[]
for k in a:
    if k not in newlist:
        newlist.append(k)
print(a)'''

a=(input("enter string"))
count={}
for k in a:
    if k in count:
        count[k]=count[k]+1
    else:
        count[k]=1
print(count)
        
