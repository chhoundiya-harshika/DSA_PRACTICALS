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

def is_balanced(text):
    stack=[]
    pairs={
        ')':'(',
        ')':'(',
        ')':'(',
        ')':'(',
        ')':'('
    }
    for i in "({{":
        stack.append(i)
    else:
        if not stack:
            return False
        if stack[-1]!=pairs.get(i):
            return False
        stack.pop()
    return len(stack)==0
print(is_balanced("{[()]}"))
print(is_balanced("([)]"))
print(is_balanced("((()"))