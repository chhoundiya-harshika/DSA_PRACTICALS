# def power(base,exponent):
#     if exponent == 0:
#         return 1
#     return base * power(base, exponent-1)
# print(power(2,4))
# print(power(3,3))

# def count_digit(n):
#     n= abs(n)
    
#     if n<10:
#         return 1
#     return 1 + count_digit(n//10)
# print(count_digit(12345))
# print(count_digit(13))
# print(count_digit(0))
def factorial(n):
    if n==0 or n==1:
        return 1
    return n* factorial(n-1)
print(factorial(6))