def power(a,x):
    if(x==0):
        return 1
    return a*power(a,x-1)
a = int(input("Enter The number: "))
b = int(input("Enter Power: "))
print(power(a,b))