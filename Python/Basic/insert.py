def Integer(a):
    a.insert(4, 5)
    return a
def String(b):
    b.insert(1, "and")
    return b
a = [1,2,3,4]
b = ["Akash","Anuj"]
print(Integer(a))
print(String(b))