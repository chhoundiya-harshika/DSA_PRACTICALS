array = [11,22,33,44,55,66]
count_odd = 0
count_even = 0
for i in array:
    if (i%2==0):
        count_even=count_even+1
    else:
        count_odd=count_odd+1
     
print(count_even)   
print(count_odd)