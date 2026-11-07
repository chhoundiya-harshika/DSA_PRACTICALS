#find the largest element from list
# num = list(map(int,input("enter numbers:").split()))
# largest = num[0]
# for i in num:
#     if i>largest:
#         largest = i
# print ("largest element from list:", largest)


#sum of all elements in list

# num = list (map(int,input("enter numbers:").split()))
# sum = 0
# for i in num:
#     if i in num:
#         sum += i
# print(sum)
    
# count the total numbers of list
num = list(map(int,input("enter numbers:").split()))
count =0
for i in num:
    if i in num:
        count +=1
print(count)
