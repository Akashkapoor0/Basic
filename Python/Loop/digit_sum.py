number = int(input("Enter A Number: "))
digit_sum = 0
for digit in str(number):
    digit_sum += int(digit)
print(digit_sum)