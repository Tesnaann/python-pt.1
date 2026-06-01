l=[2,10,12,16,3] #arrange given list in order(increasing)
length=5
for i in range(length):
 for j in range(length-i-1):
  print("j=",j)
  if l[j]>l[j+1]:
   l[j],l[j+1]=l[j+1],l[j]
  print(l) 