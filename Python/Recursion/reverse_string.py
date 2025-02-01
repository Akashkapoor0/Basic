def reverse(a):
    if len(a) == 0:
        return a
    else:
        return a[-1] + reverse(a[:-1])
a = input("Enter String: ")
print("The Reverse String is:", reverse(a))