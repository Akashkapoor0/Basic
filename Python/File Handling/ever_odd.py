f1 =  open("example", "r")
a= f1.read().split()
f2=  open("odd.txt", "w")
f3 = open("even.txt", "w")
for i in range(len(a)):
    if i % 2 == 0:
        f2.write(a[i])
    else:
        f3.write(a[i])
