import math
pi = math.pi

def sphere_volume():
    """ Calculating volume of a sphere """
    r = int(input("Enter r that you want to calculate the volume of a sphere: "))
    return 4/3 * pi * (r**3)

print(sphere_volume())
print(sphere_volume.__doc__)
