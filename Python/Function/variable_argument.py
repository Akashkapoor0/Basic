def variable_arguments(*a,**k):
    print("Positional arguments:", a)
    print("Keyword arguments:", k)
variable_arguments(1, 2, 3, a=4, b=5)