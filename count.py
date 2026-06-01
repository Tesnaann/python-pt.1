#how many times a letter is repeated
word=(input("enter string"))
count=dict()
for k in word:
    if k in count:
        count[k]=count[k]+1
    else:
        count[k]=1
    print(count)