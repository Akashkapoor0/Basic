from functools import reduce
def Sum(lst):
    return reduce(lambda x, y: x + y, lst)

numbers = [1, 2, 3, 4, 5]
result = Sum(numbers)
print("Sum of all elements:", result)