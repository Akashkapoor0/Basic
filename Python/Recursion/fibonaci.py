def fibo(a):
    if a == 0 or a ==1:
        return a
    return fibo(a-1) + fibo(a-2)

n = int(input("Enter Nubmer: "))
for i in range(n):
    print(fibo(i),end=" ")