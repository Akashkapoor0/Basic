def rhombus(diagonal1, diagonal2):
    return (diagonal1 * diagonal2) / 2

def trapezium(base1, base2, height):
    return ((base1 + base2) * height) / 2

def parallelogram(base, height):
    return base * height

d1 = 5
d2 = 6
print(f"Area of Rhombus: {rhombus(d1, d2)}")

b1 = 3
b2 = 4
h = 5
print(f"Area of Trapezium: {trapezium(b1, b2, h)}")

base = 4
height = 5
print(f"Area of Parallelogram: {parallelogram(base, height)}")