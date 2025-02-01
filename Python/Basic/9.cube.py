
side = 5
cube_volume = side ** 3
cube_surface_area = 6 * (side ** 2)

length = 5
width = 3
height = 4
cuboid_volume = length * width * height
cuboid_surface_area = 2 * (length * width + width * height + height * length)


radius = 3
height = 7
pi = 3.14
cylinder_volume = pi * (radius ** 2) * height
cylinder_surface_area = 2 * pi * radius * (radius + height)

print("Cube Volume:", cube_volume)
print("Cube Surface Area:", cube_surface_area)
print("Cuboid Volume:", cuboid_volume)
print("Cuboid Surface Area:", cuboid_surface_area)
print("Cylinder Volume:", cylinder_volume)
print("Cylinder Surface Area:", cylinder_surface_area)