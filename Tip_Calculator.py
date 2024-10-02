# 9/24/19 make a program with 2 functions and a main function.
# Function #2 has to print the information obtained in function #1.
# Function #1 will calculate the tip of a dinner of 5 course plate
# and Function #2 will receive the value of the 5-course dinner,
# the tax, and the tip and show it to the user.

def tip_calc(percent):
    sub_total = 0
    for i in range(5):
        course_num = str(i + 1)
        course = float(input("Please enter the cost of course " + course_num + ": "))
        sub_total += course
    print("Your subTotal for the 5 course dinner is", sub_total)
    tax = sub_total * 0.08
    print("The tax (8%) is", tax)
    tip = sub_total * percent * 0.01
    print("The tip is", tip)
    total = sub_total + tax + tip
    print("The total price is", total)


def func2():
    tip_percent = float(input("Please enter the percentage (%) you will tip: "))
    tip_calc(tip_percent)


def main():
    func2()


main()
