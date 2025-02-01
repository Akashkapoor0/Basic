l = [1,2,3,4,5,6,7,8,9,10]
def evenno(n):
    if(n%2==0):
        return True
y = list(filter(evenno,l))
print(y)