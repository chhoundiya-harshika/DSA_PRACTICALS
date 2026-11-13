def power(base,exponet):
    if exponet == 0:
        return 1
    return base * power(base, exponet-1)
print(power(2,4))
print(power(3,3))