f = open("example","r")
a = f.read()
f = open("example1","w")
b = f.write(a)
print("done")
f.close