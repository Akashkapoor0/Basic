x = 20
def outer():
    x = 10
    def inner():
        x = 5
        print(x)
    return inner()
y = outer()