def add_list(a):
    for i in range(1,11):
        a.append(int(input()))
    return a
lst = []
print(add_list(lst))