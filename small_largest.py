# array = [11,44,22,66]
# sorted_array=sorted(array)

# second_smallest = array[2]
# second_largest = array[-3]

# print("second smallest element:", second_smallest )
# print("second largest element:", second_largest )

arr=[10,42,8,6,13]
min=smin=arr[0]
max=smax=arr[0]
for num in arr:
    if num>max:
        smax>max
        max=num
    elif(num>smax and num!=max):
        smax=num
    if num<min:
        smin=min
        min=num
    e