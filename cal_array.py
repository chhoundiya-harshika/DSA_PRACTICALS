#Write a program to accept N integers into an array and calculate & display the sum

N=int(input("Enter a an integer"))
sum=0
for i in range(1,N+1):
    sum =sum +i
    print(sum)
