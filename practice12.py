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
# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     return n* factorial(n-1)
# print(factorial(6))

#sum of natural numbers with recursion

# def sum_natural(n):
#     if n==0:
#         return 0
#     return n+sum_natural(n-1)
# print(sum_natural(10))

# def fibonacci(n):
#     if n==0:
#         return 0
#     if n==1:
#         return 1
#     return fibonacci(n-1)+fibonacci(n-2)
# for i in range(7):
#     print(fibonacci(i), end= " ")

# countdown
def countdown(n):
    if n==0:
        print("Done!")
        return 
    print(n)
    countdown(n-1)
countdown(10)