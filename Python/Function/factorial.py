def fact(a):
    sum = 1
    for i in range(1,a+1):
        sum *=i
    return sum
a = int(input("Enter Number : "))
print("Factorial is",fact(a))