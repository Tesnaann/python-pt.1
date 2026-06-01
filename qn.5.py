#anagram-same spelling w different arrangement to form words

word1="silent"
word2="listen"
sorted_1=sorted(word1)
sorted_2=sorted(word2)
if len(word1)!=len(word2):
    print("Not anagram")
elif sorted_1==sorted_2:
    print("Anagram")






