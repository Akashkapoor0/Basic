sum = 0
for num in range(1,101):
    if num > 1:
        i = 2
        is_prime = True
        while i < num:
            if (num % i) == 0:
                is_prime = False
                break
            i += 1
        if is_prime:
            sum+=num
            print(num," ", end= "")
print()
print("Prime sum is",sum)            