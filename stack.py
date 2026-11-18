# # implement a stack using python

# stack=[]
# #push
# stack.append(10)
# stack.append(20)
# stack.append(30)
# stack.append(40)
# stack.append(50)
# stack.append(60)
# print(stack)

# # pop
# stack.pop()

# print(stack)

# # peek
# print(stack[-1])

# def is_balanced(text):
#     stack=[]
#     pairs={
#         ')':'(',
#         ')':'(',
#         ')':'(',
#         ')':'(',
#         ')':'('
#     }
#     for i in "({{":
#         stack.append(i)
#     else:
#         if not stack:
#             return False
#         if stack[-1]!=pairs.get(i):
#             return False
#         stack.pop()
#     return len(stack)==0
# print(is_balanced("{[()]}"))
# print(is_balanced("([)]"))
# print(is_balanced("((()"))

# def reverse_string(text):
#     stack=[]
#     for i in text:
#         stack.append(i)
#     result=""
    
#     while stack:
#         result+=stack.pop()
#     return result
# print(reverse_string("python"))

class stack:
    def __init__(self):
        self.item=[]
    def push (self,value):
        self.item.append(value)
    def pop(self):
        if self.is_empty():
            return None
        return self.item.pop()
    def peek(self):
        if self.is_empty():
            return None
        return self.item[-1]
    def is_empty(self):
        return len(self.item)==0
    
s = stack()
s.push(10)   
s.push(20)   
s.push(30)   

print(s.peek())
print(s.pop())
print(s.peek())
print(s.is_empty())
            