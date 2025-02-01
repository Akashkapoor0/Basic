l = ['1-SAN\n','2-BAN\n','3-RAN\n','4-JAN']
f = open("example",'w')
f.writelines(l)
f.close()
f = open("example","r")
s = f.read()
print(s)
f.close()
