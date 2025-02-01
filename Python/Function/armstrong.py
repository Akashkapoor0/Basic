def armstrong():
    for num in range(1, 201):
        order = len(str(num))
        total = 0
        temp = num
        while temp > 0:
            digit = temp % 10
            total += digit ** order
            temp //= 10
        if num == total:
            print(num)
armstrong()