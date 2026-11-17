#hashing and dictionary
# def two_sum(arr, target):
#     seen = {}
#     for i in range(len(arr)):
#         complement = target - arr[i]
        
#         if complement is seen:
#             return [seen[complement],i]
#         seen [arr[i]]=i
#     return []
# print(two_sum([2,7,11,15],9))
# print(two_sum([3,2,4],6))
        
#find duplicate elements in an array

# def find_duplicates(arr):
    
#     seen = set()
#     duplicates = set()
    
#     for num in arr:
#         if num in seen:
#             duplicates.add(num)
#         else:
#             seen.add(num)
#     return list (duplicates)
# print(find_duplicates([1,2,3,2,4,5,1]))
            

#find the first non repeating character

def first_non_repeating(text):
    freq={}
    for ch in text:
        freq[ch]=freq.get(ch,0)+1
    for ch in text:
        if freq[ch]==1:
            return ch
    return None
print(first_non_repeating("swiss"))
print(first_non_repeating("aabb"))