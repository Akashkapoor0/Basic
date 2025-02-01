def binary():
    num = int(input())
    bnum = ""
    while num > 0:
        bnum= str(num % 2) + bnum
        num = num // 2
    print(bnum)
binary()