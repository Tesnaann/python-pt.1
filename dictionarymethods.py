#get,return value for given key
a={"name":"Tesna","age":19}
print(a.get("name"))
#update
a.update(place="kochi")
print(a)
#pop-remove specified value
(a.pop('name'))
print(a)
#popitem-remove last key and value
a.popitem()
print(a)

#items -provide key with values
student={"name":"Tesna","age":19}
for k,i in student.items():
    print(k,i)

print(student.items())

#clear()Removes all items from the dictionary

#get()Returns the value for the given key
print(student.get("age"))

#keys()Returns a view object that displays a
#list of all the keys in the dictionary in order of insertion
print(student.keys())


#values()
print(student.values())



