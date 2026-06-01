#character frequency count, count how many times each character appear in a list
word="programming"
count=dict()
for k in word:
    if k in count:
        count[k]=count[k]+1
    else:
        count[k]=1
print(count)