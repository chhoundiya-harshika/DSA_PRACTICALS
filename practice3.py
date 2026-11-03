from typing import Union

def calculate(a: int, b: int, op: str)-> Union[int, float, str]:
    if op == "+":
        return a+b
    elif op == "-":
        return a-b
    elif op == "*":
        return a*b
    elif op == "/":
        if b==0:
            return "Division by zero"
        return (a/b,2)
    elif op == "//":
        if b==0:
            return "Division by zero"
        return (a%b)
    else:
        return "invalid operator"
    