# Ask the user for an integer and check the input validation and after
# the number is correct elevate the number to power 7. Make 2 functions

import math         # imports the math module


def check_input():
    # fn verifies that the integer is positive, if it is not, it will prompt
    # the user to try again. Once there is a positive integer, power of 7
    num = input("Enter an integer: ")
    x = 0
    while x == 0:
        if num.lstrip('-').isdigit():
            print("Number accepted, elevating to power of 7...\n")
            num = int(num)
            num = pow(num, 7)
            print(num)
            x = 1
        else:
            print("That is not an expected value.")
            num = input("Enter an integer: ")


def main():
    check_input()


main()
