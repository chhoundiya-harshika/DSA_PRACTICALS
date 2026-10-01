row,col =5,5
for i in range (row):
    for j in range (col):
        if(i+j)%2 == 0:
            print("1", end="")
        else:
            print("0", end="")
    print()