'''rows=6
for r in range(1,rows+1):
    num=r
    n=rows-1
    for c in range(r):
        print(num,end=" ")
        num+=n
        n-=1
    print("")'''
rows=6
for r in range(1,rows+1):
    num=r
    n=rows-1
    for k in range(r):
     print(num,end="")
     num=num+n
     n-=1
    print("")


