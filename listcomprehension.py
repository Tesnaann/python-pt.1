#List comprehension is a concise and powerful way to create new lists by applying an 
# expression to each item in an existing iterable (like a list, tuple or range                                                                                                                                    
#when you want to create a new list based on the values of an existing list.


#to print even nums
even=[num for num in range(1,50) if num%2==0]
print(even)