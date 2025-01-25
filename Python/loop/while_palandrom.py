a = 13431
r = 0
rev= 0
b = a
while(a>0):
    r = a%10
    rev = rev*10+r
    a= a//10
if(rev==b):
    print("Pallendrom")
else:
    print("not Palandrom")