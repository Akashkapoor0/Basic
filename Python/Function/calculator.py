def calculator(a,b,c):
    if(c == "+"):
        return a+b
    if(c == "-"):
        return a-b
    if(c == "/"):
        return a/b
    if(c == "*"):
        return a*b
a = int(input("Enter A: "))
c = input("Enter Oprator: ")
b = int(input("Enter B: "))
print(f"{a} {c} {b} = {calculator(a,b,c)}" )