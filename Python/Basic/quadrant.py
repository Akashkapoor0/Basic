x = float(input("Enter the x coordinate: "))
y = float(input("Enter the y coordinate: "))
if x > 0 and y > 0:
    print("The point on first quadrant.")
elif x < 0 and y > 0:
    print("The point on second quadrant.")
elif x < 0 and y < 0:
    print("The point on third quadrant.")
elif x > 0 and y < 0:
    print("The point on fourth quadrant.")
elif x == 0 and y != 0:
    print("The point is on the y-axis.")
elif y == 0 and x != 0:
    print("The point is on the x-axis.")
else:
    print("The point is at the origin.")
