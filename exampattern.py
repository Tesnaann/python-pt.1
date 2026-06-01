'''row=4
cpol=6
for i in range(row):
    for j in range(cpol):
        print("*",end="")
    print()      '''       #rect w 4 rows and 6 col

for i in range(5):
    for j in range(5):
        if i==0 or i==4 or j==0 or j==4:
            print("*",end="")
        else:
            print(" ",end="")
    print()