#bubble sort in descending order
l=[5,10,8,4,2]
length=5
for i in range(length):
 for j in range(length-i-1):
  print("j=",j)
  if l[j]<l[j+1]:
   l[j],l[j+1]=l[j+1],l[j]
  print(l) 
