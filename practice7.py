# numbers = [10,20,30,40,50]
# target = 40
# for i in range(len(numbers)):
#     if numbers[i]==target:
#         print("Fount at index:", i)
#         break

# def binary_search(arr,target):
#     low=0
#     high= len(arr)-1
    
#     while low<=high:
#         mid = (low+high)//2
        
#         if arr[mid]==target:
#             return mid
#         elif arr[mid]<target:
#             low = mid+1
#         else:
#             high = mid-1
#     return -1
# numbers = [10,20,30,40,50]
# print(binary_search(numbers,40))

def linear_search(arr, target):
     
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
arr = [5,10,15,20]
print(linear_search(arr,10))
    
        