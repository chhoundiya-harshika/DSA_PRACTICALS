# #Anagram

# def are_anagram(s1,s2):
#     s1=s1.replace(" "," ").lower()
#     s2=s2.replace(" "," ").lower()
    
#     if len(s1)!=len(s2):
#         return False
    
#     freq = {}
#     for ch in s1:
#         freq[ch]=freq.get(ch,0)+1
#     for ch in s2:
#         if ch not in freq:
#             return False
        
#         if freq[ch]<0:
#             return False
#     return True
# print(are_anagram("listen","silent"))
# print(are_anagram("hello","world"))
# print(are_anagram("debir card","bad credit"))

#reverse a string without slicing
# def reverse_string(text):
    
#     result =""
#     for ch in text:
#         result = ch + result
#     return result
# print(reverse_string("python"))

# arr = [10,20,30,40,50]
# left = 0
# right = len(arr)-1
# print(arr[left])
# print(arr[right])

def reverse_array(arr):
    left = 0
    right = len(arr)-1
    
    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        
        left +=1
        right -=1
    return arr
numbers = [10,20,30,40]
print(reverse_array(numbers))