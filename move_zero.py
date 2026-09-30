#move_zero to the end 
array = [1,0,2,0,3,0,4]
index=0
for i in range(len(array)):
    if (array[i]!=0):
        array[index]=array[i]
        index = index+1
        
for i in range(index, len(array)):
    array[i]=0
print(array)
    