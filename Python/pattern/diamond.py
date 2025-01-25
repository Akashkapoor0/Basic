n = int(input("Enter Number : "))
for i in range(1,n):
    print(f"{" "*(n-i-1)}{"x"*(i*2-1)}")   
for i in range(n-1,1,-1):
    print(f"{" "*(n-i)}{"x"*(i*2-3)}")
