a=[12,13,14,15,16,17]
for k in a:
    if k<=1:
        pass#is used to skip into nxt without printing
    else:
        for g in range(2,k):
            if k%g==0:
                break
        else:
            print(k)
