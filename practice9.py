# name = "Python"
# company = "Google"

# print(name)
# print(company)

# text = "PYTHON"

# print(text[0])
# print(text[1])
# print(text[2])
# print(text[3])

#string traversal
# text= "Python"
# for i in text:
#     print(i)

#reverse the string
# text = "hello"
# print(text[::-1])

# def reverse_string(text):
#     reversed_text=""
#     for i in text:
#         reversed_text = i + reversed_text
#     return reversed_text
# print(reverse_string("hello"))
# print(reverse_string("python"))

text = "Programming"
for ch in set (text):
    print(ch, text.count(ch))