#find largest element from array

# arr = [10,20,30,40]

# largest=arr[3]

# for num in arr:
#     if num>largest:
#         largets=num
# print(largest)
        
#second largest

def second_largest(arr):
    largest= None
    second=None
    
    for num in arr:
        if largest is None or num>largest:
            second=largest
            largets=num
        elif num != largest:
            if second is None or num>second:
                second=num
    return second
arr = [10,20,30,40]

result=second_largest(arr)

if result is None:
    print("No second-largest element")
else: 
    print(result)