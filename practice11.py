#find largest element from array

# arr = [10,20,30,40]

# largest=arr[3]

# for num in arr:
#     if num>largest:
#         largets=num
# print(largest)
        
#second largest

# def second_largest(arr):
#     largest= None
#     second=None
    
#     for num in arr:
#         if largest is None or num>largest:
#             second=largest
#             largets=num
#         elif num != largest:
#             if second is None or num>second:
#                 second=num
#     return second
# arr = [10,20,30,40]

# result=second_largest(arr)

# if result is None:
#     print("No second-largest element")
# else: 
#     print(result)

# def find_missing(arr,n):
#     expected=n*(n+1)//2
#     actual=sum(arr)
    
#     return expected-actual
# print(find_missing([1,2,3,5],5))

def move_zero(arr):
    position = 0
    
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[position]=arr[i]
            position+=1
    while position<len(arr):
        arr[position]=0
        position+=1
    return arr
numbers=[0,1,0,3,12]
print(move_zero(numbers))