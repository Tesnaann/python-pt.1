#find second largest number without sort()
'''a=[10,5,20,]
c=max(a)
print(c)
a.remove(c)
d=max(a)
print(d)'''
 

'''a=[10,5,20,8,15]
l=len(a)
for i in range(1,l+1):
    for j in range(i+1,l):
        if (a[i]>a[j]):
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print(a[-2])'''


a=[10,5,20,8,15]
largest= a[0] #first element of list a =0
second=a[0]
for num in a[1:]:# elements from 1st position to the end
    if num>largest:
        second=largest
        largest=num
    elif num>second:
        second=num
print(second)
    







