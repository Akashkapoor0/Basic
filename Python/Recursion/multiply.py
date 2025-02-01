def multi(a, b):
    if b == 0:
        return 0
    elif b > 0:
        return a + multi(a, b - 1)
    else:
        return -multi(a, -b)
a = int(input("Enter A = "))
b = int(input("Enter B = "))
print(multi(a,b))