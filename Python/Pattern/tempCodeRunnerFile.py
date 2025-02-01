n = int(input("Enter Number : "))
for i in range(1, n + 1):
    print(f"{' ' * (n - i)}{'x' * (i * 2 - 1)}")
for i in range(n - 1, 0, -1):
    print(f"{' ' * (n - i)}{'x' * (i * 2 - 1)}")
