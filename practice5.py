# def is_palindrome(n):
#     if n<0:
#         return False
    
#     original = n
#     reverse = 0
#     while n>0:
#         digit = n%10
#         reverse = reverse *10 + digit
#         n = n// 10
#     return original == reverse
# num = int (input("Enter a number:"))

# if is_palindrome(num):
#     print ("Palindrome")
# else: 
#     print("Not palindrome")

def factorial(n):
    fact=1
    for i in range(1, n+1):
        fact = fact * i 
    return fact
print(factorial (5))
