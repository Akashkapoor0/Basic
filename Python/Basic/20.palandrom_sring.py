def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
t = "akashsaka"
print(is_palindrome(t))