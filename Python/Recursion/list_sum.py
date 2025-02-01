def sSum(a):
    if len(a) == 1:
        return a[0]
    return a[0] + sSum(a[1:])

a = [1, 5, 7, 6, 8, 2]
print("Sum is",sSum(a))