def num(n):
    if(n == 0):
        return 0
    return n+num(n-1)
n = int(input("Enter Number: "))
print("sum is",num(n))