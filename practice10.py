#Anagram

def are_anagram(s1,s2):
    s1=s1.replace(" "," ").lower()
    s2=s2.replace(" "," ").lower()
    
    if len(s1)!=len(s2):
        return False
    
    freq = {}
    for ch in s1:
        freq[ch]=freq.get(ch,0)+1
    for ch in s2:
        if ch not in freq:
            return False
        
        if freq[ch]<0:
            return False
    return True
print(are_anagram("listen","silent"))
print(are_anagram("hello","world"))
print(are_anagram("debir card","bad credit"))