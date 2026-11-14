# reverse string using recursion

# def reverse_string(text):
#     if len(text)<=1:
#         return text
#     return reverse_string (text[1:])+text[0]
# print(reverse_string("pythhon"))

# greates common divisor

def gcd(a,b):
    if b==0:
        return a
    return gcd(b, a%b)
print(gcd(12,18))