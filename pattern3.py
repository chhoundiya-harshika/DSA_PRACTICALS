n=9
mid = n//2
for i in range(n):
    for j in range(n):
        if j==abs(mid-1) or j==(n-1) - abs(mid-i):
            print("*", end = " ")
        else:
            print(" ", end=" ")
    print()