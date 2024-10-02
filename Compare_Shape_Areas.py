# Create a program in Python with 3 functions. Function 1 will
# calculate the area of a rectangle, function 2 the area of a circle, and
# function 3 will subtract the area of the circle from the rectangle
# area rectangle = height * width (height is 24 width is 36)
# area circle = pi r squared (r is 15)

import math


def area_rectangle(h, w):
    return h * w


def area_circle(r):
    return math.pi * pow(r, 2)


def subtract():
    x = str(round(area_rectangle(24, 36) - area_circle(15), 2))
    print("difference of rectangle area and circle area: " + x)


def main():
    subtract()


main()
