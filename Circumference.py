import math


def circumference(r):
    # creates fn for finding circumference of circle
    return 2 * math.pi * r


radius = int(input("Enter the radius of the circle: "))
print("The circumference of the circle is: ", round(circumference(radius), 2))


# Other Way
def circumference(r):
    # puts the print statement inside the function
    c = 2 * math.pi * r
    print("the circumference of the circle is: ", round(c, 2))


radius = int(input("enter the radius of the circle: "))
circumference(radius)
