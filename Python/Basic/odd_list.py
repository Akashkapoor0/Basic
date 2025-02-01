a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0

while i < len(a): 
    if a[i] % 2 == 0:
        a.pop(i)
    else:
        i += 1 

print(a)
