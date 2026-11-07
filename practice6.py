#find the largest element from list
num = list(map(int,input("enter numbers:").split()))
largest = num[0]
for i in num:
    if i>largest:
        largest = i
print ("largest element from list:", largest)

    