def power(base, exp):
    if exp == 0:
        return 1
    elif exp > 0:
        return base * power(base, exp - 1)
    else:
        return 1 / power(base, -exp)
a = int(input("Enter Base: "))    
b = int(input("Enter Power: "))
result = power(a, b)
print("Answer is", result)