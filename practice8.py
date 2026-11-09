#bubble sort
# arr =[5,3,8,1,2]
# for i in range(len(arr)-1):
#     for j in range(0,len(arr)-i-1):
#         if arr[j]>arr[j+1]:
#             arr[j], arr[j+1]=arr[j+1], arr[j]
# print(arr)
        
        
#selection sort

arr=[63,25,12,22,11]
for i in range(len(arr)):
    min_index=i
    
    for j in range(i+1, len(arr)):
        if arr[j]<arr[min_index]:
            min_index=j
            
    arr[i], arr[min_index]=arr[min_index],arr[i]
    print(arr)
