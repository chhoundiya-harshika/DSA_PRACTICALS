# def subtractProductAndSum (n: int)->int:
n=44
prod = 1
sum = 0
while n>0:
    digit=n%10
    prod*=digit
    sum+=digit
    n=n//10
print(prod-sum)
# return prod - sum