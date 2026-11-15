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
# def frequency_count(text):
#     freq={}
#     for i in text:
#         if i in freq:
#             freq[i]+=1
#         else:
#             freq[i]=1
            
        
#        git add .
# return freq
# print(frequency_count("Programmingp"))

# duplicate 

# def remove_duplicate(arr):
#     seen = set()
#     result=[]
#     for num in arr:
#         if num not in seen:
#             seen.add(num)
#             result.append(num)
#     return result
    
# print(remove_duplicate([1,2,2,3,3,4,5,6,7,7,8]))
    
def common_elements(arr1,arr2):
    set1 = set (arr1)
    set2= set(arr2)
    
    return set1.intersection(set2)
print(common_elements([1,2,3,4,5],[3,4,5,6,7]))