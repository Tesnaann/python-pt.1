import re  #re is regular expression
txt="it's not just 2 about ideas 123 its about making ideas happen do it"
result=re.search('just',txt)
print(result) #output-(9,13)
'''result1=re.match(r"\d",txt) #\d is used to print digits,\d+ is used to print individually
print(result1)

word="Hello 22 how are you"
res=re.findall(r"[A-Z a-z\d]+",word)
print(res)'''
