#merge two dictionaries
'''d1={'a':10,'b':20}
d2={'b':5,'c':15}
merged={}
#add values from first dict
for key in d1:
    if key in d2:
        merged[key]=d1[key]+d2[key]
    else:
        merged[key]=d1[key]
    #add remaining key from second dict
    for k in d2:
        if key not in merged:
            merged[key]=d2[key]
    print(merged)'''

d1={'a':10,'b':5}
d2={'b':10,'c':20}
merged={}
for key in d1:
    if key in d2:
        merged[key]=d1[key]+d2[key]
    else:
        merged[key]=d1[key]
for key in d2:
    if key not in merged:
        merged[key]=d2[key]
print(merged)


