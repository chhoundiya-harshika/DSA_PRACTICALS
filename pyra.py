# n=5
# for i in range(1,n+1):
#     for space in range(1, (4-i)*2 +1):
#         print(" ", end = " ")
#     for j in range (1, i+1):
#         print(j, end=" ")
#     print("1")
#     print()
        
# n=5
# sp=5
# for i in range(1,n+1):
#     for s in range(0, sp):
#         print(end=" ")
#     for j in range(1, i+1):
#         print(j, end=" ")
#     if(i!=1):
#         print("1")
#     print()
#     sp-=1

# n = int(input("Enter a num:"))
# for i in range(n):
#     for j in range(1,i+1):
#         print(chr(64+j), end=" ")
#     print()
    
# n = int(input("Enter a num:"))
# for i in range(n):
#     for j in range(1,i+1):
#         print(chr(64+i), end=" ")
#     print()
    
# n = int(input("Enter a num:"))
# num=0
# for i in range(n):
#     for j in range(1,i+1):
#         print(chr(65+num), end=" ")
#         num+=1
#     print()

# n = int(input("Enter a num:"))
# for i in range(n):
#     print('  '*(n-i+1), end ="")
#     for j in range(2*i+1):
#             print(chr(65+j), end=" ")
#     print()

# n = int(input("Enter a num:"))
# for i in range(n):
#     print('  '*(n-i+1), end="")
#     for j in range (2*i+1):
#        if (j==0 or j==2*i or i==n-1):
#            print(chr(65+j), end=" ")
#        else:
#            print(" ", end=" ")
#     print()

n=7
mid=(n+1)//2

for i in range(n):
    for j in range(n):
        if(j==mid or i==mid):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()