l=[8,4,2,1,7]
length=5
for i in range(length):
    for j in range(length-i,1):
      if l[j]>l[j+1]:
         l[j],l[j+1]=l[j+1],l[j] 

#descending order