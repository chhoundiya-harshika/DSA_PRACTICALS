array=[1,2,3,4,5]
search=0
position =-1
num = int(input("Enter a num"))
for index, i in enumerate(array):
    if(num==i):
        search=1
        position=index
        break
if search:
    print(f"Yes, element {num} is in the array and the position of an array is {position}!")
else:
    print(f"No, element {num} is NOT in the array.")