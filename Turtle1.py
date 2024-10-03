import turtle


def color_square_1(a, b):
    # function with a loop that will create a square filled a color
    t1.fillcolor(b)
    t1.begin_fill()
    for i in range(4):
        t1.forward(a)
        t1.left(90)
    t1.end_fill()


t1 = turtle.Turtle()
color_square_1(50, 'lightgreen')


turtle.done()
