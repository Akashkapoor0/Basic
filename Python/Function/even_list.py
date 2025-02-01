def Even(a):
    even = []
    for i in a:
        if i % 2 == 0:
            even.append(i)
    return even

a = [1,2,3,4,5,6,7,8,9,10]
print(Even(a))