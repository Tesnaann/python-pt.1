numbers=[12,45,2,7]
def multiply(num):
    return num*2
l=list(map(multiply,numbers))  # map is used to iterate without for loop
print(l)

number=[12,45,2,7,8]
l=list(map(lambda num:num*2,number))
print(l)
#map -- map provide boolean value so filter is used

number=[12,45,2,7,8]
l=list(filter(lambda num:num%2==0,number))
print(l)

num=(12,4,5,8)
l=tuple(map(lambda x:x,number))
print(l)