a = 153
arm = 0
r = 0
t= len(str(a))
while(a>0):
    r = a%10
    a//=10
    arm += r**t
print(arm)
if(arm == a):
    print("its Armstrong number")
else:
    print("Not Armstrong")