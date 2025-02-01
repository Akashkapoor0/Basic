l = ['Mohan','Akash','Sita','San']
def check(n):
    if(type(n) == str):
        return True
    return False
def chklen(n):
    if(len(n)>=4):
        return True
    return False
y = list(filter(chklen,l))
print(y)