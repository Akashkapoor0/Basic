def unique(input_list):
    u= []
    for element in input_list:
        if element not in u:
            u.append(element)
    return u
i = [1, 2, 2, 3, 4, 4, 5]
u = unique(i)
print("Original list:", i)
print("Unique list:", u)