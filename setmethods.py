k={2,34,5,6,2,22,"kochi"}
#add
k.add(55)
print(k)


#remove,The remove() method raises a KeyError 
# if the specified item is not found in the set.
k.remove(2)
print(k)


#pop,o there's no guarantee which element will
#be removed and returned by the pop() method. 
k.pop()
print(k)


#k.pop(5)
#print(k)



#discard-method does nothing 
#and does not raise an error if the specified item is not found. 
k.discard(99)
print(k)
#intersection
B={34,5,6,66,78}
print(k.intersection(B))
