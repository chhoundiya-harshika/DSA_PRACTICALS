#count the each ch in string
def character_frequency (text):
    freq = {}
    for i in text:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    return freq
print(character_frequency("heyy"))
print(character_frequency("cherry-cosmos"))
        