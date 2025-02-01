n = input("Enter a number: ")
try:
    complex(n)
    print("Factorial does not exist for complex numbers")
    exit()
except ValueError:
    n = int(n)
fact = 1
if n < 0:
    print("Factorial does not exist for negative numbers")
else:
    for i in range(1, n + 1):
        fact *= i
    print(f"The factorial of {n} is {fact}")