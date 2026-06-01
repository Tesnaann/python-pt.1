#to combine two or more iterables (like lists, tuples, strings, dictionaries, etc.) into
#  a single iterator 
a=["name","age",66]
b=["Tesna",75,99]
c=list(zip(a,b))
print(c)
d=tuple(zip(a,b))
print(d)
e=dict(zip(a,b))
print(e)
