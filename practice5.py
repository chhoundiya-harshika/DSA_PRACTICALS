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

# def factorial(n):
#     fact=1
#     for i in range(1, n+1):
#         fact = fact * i 
#     return fact
# print(factorial (5))

def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
        return True
print(is_prime(6))
print(is_prime(7))
       
