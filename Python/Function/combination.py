def fact(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def ncr(n, r):
    return fact(n) / (fact(r) * fact(n - r))
n = 5
r = 3
print(ncr(n, r))