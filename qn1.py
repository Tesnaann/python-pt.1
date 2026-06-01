#remove duplicate item without fn set()
a=[1,2,2,3,4,3,5]
nlist=[]
for k in a:
    if k not in nlist:
        nlist.append(k)
print(nlist)

