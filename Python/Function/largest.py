from functools import reduce
def find(numbers):
    return reduce(lambda a, b: a if a > b else b, numbers)
numbers = [3, 5, 2, 8, 1]
largest = find(numbers)
print(f"The largest number is: {largest}")