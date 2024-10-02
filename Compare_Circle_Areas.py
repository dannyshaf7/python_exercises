# Create a program in python that calculates the area of 2 circles
# and give you which one is the biggest. Area of circle = 3.14 * r^2
import math


def larger_area():
    area1 = round(math.pi * pow(radius1, 2), 2)
    print("The Area of Circle 1 is: ", area1)
    area2 = round(math.pi * pow(radius2, 2), 2)
    print("The Area of Circle 2 is: ", area2)
    if area1 > area2:
        print("The Area of Circle 1 is larger.")
    elif area2 > area1:
        print("The Area of Circle 2 is larger.")
    else:
        print("The Areas of Circles 1 and 2 are equal.")


radius1 = int(input("Please enter the radius of Circle 1: "))
radius2 = int(input("Please enter the radius of Circle 2: "))
larger_area()
