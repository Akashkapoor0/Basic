def name():
    return "Akash"
def outer(name):
    def inner():
        x = name()
        print("Hi",x)
    return inner()
y = outer(name)