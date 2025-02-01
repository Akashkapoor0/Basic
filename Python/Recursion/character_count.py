def count(a,ch):
    if(len(a)==0):
        return 0
    if(a[0] == ch):
        return 1+count(a[1:],ch)
    else:
        return count(a[1:],ch)
a = input("Enter String: ")
b = input("Enter Character: ")
print("Character Count: ",count(a,b))