def _low(s):
    result = ""
    for c in s:
        if 'A' <= c <= 'Z':
            result += chr(ord(c) + 32)
        else:
            result += c
    return result

def _upp(s):
    result = ""
    for c in s:
        if 'a' <= c <= 'z':
            result += chr(ord(c) - 32)
        else:
            result += c
    return result


s = "Hello World"
print(_low(s)) 
print(_upp(s))  