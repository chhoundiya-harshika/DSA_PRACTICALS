# student = {
#     "name":"Rahul",
#     "age": 26,
#     "marks": 86
# }

# print(student["name"])
# print(student["marks"])

#basic operations

# numbers= {1,2,2,3,4,4}
# print(numbers)

# a={1,2,3,4}
# b={3,4,5,6}

# print(a.union(b))
# print(a.intersection(b))
# print(a.difference(b))

# count each charater in dict
def frequency_count(text):
    freq={}
    for i in text:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
            
        
        return freq
print(frequency_count("Programmingp"))

    