def one(msg):
    return msg+"1"
def two(msg):
    return msg+"2"
def three(fun):
    x = fun("msg inside")
    print(x)
three(one)
three(two)