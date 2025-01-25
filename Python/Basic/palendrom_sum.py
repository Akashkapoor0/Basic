a = input("Enter a string: ")

palandrom = a == a[::-1]

if palandrom:
    result = ord(a[0]) + ord(a[-1])
    print("The input is a palindrome.")
    print(f"Sum of ASCII values of first and last character: {result}")
else:
    print("Not Palandrom")