def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])

a = reverse_string("Akash Kapoor")
print(a)