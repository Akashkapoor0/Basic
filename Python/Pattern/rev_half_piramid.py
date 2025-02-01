n = int(input("Enter the number: "))+1
for i in range(1,n):
    for j in range(1,n-i+1):
        print("x", end = " ")
    print()