n = 8
for i in range(n):
    for j in range(n - i):
        print(" ", end="")
    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i or i == n // 2:
            print("x", end="")
        else:
            print(" ", end="")
    print()
