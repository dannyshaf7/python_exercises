import math


def area(a, b):
    # creates fn for finding area with 2 parameters
    return a * b     # returns result of parameter1*parameter 2 (formula for area)


height = int(input("Enter the object height: "))  # assigns input to variable 1
width = int(input("Enter the object width: "))   # assigns input to variable 2
print(area(height, width))    # prints call for area fn with specified parameters


# Alternative #
def area(w, h):
    # puts the print statement inside the function
    a = w * h
    print("the area of the figure is", a)


width = input("enter the width of the figure: ")
width = int(width)
height = input("enter the height of the figure: ")
height = int(height)
area(width, height)


# area of circle
def area(r):
    return math.pi * r ** 2


radius = int(input("Enter the radius of the circle: "))
print("The area of the circle is: ", round(area(radius), 2))


# alternative
def area(r):
    # puts the print statement inside the function
    a= math.pi * math.pow(r, 2)
    print("the area of the circle is: ", round(a, 2))


radius = int(input("enter the radius of the circle: "))
area(radius)
