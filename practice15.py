#hashing and dictionary
def two_sum(arr, target):
    seen = {}
    for i in range(len(arr)):
        complement = target - arr[i]
        
        if complement is seen:
            return [seen[complement],i]
        seen [arr[i]]=i
    return []
print(two_sum([2,7,11,15],9))
print(two_sum([3,2,4],6))
        

