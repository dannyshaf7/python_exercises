# Write a program that is consisting of three functions:
#  - main() function, prompts the user to enter three numbers, sends these
#    numbers to function1() as arguments
#  - Function1(), takes three numbers, finds the maximum, and then sends those
#    three numbers with the maximum to function2()
#  - Function2(), takes four numbers, and returns the minimum to function1()


def max_val(num_1, num_2, num_3):
    if num_1 > num_2 and num_1 > num_3:
        maximum = num_1
    elif num_2 > num_1 and num_2 > num_3:
        maximum = num_2
    else:
        maximum = num_3
    return maximum, min(num_1, num_2, num_3)


def min_val(num_1, num_2, num_3):
    if num_1 < num_2 and num_1 < num_3:
        minimum = num_1
    elif num_2 < num_1 and num_2 < num_3:
        minimum = num_2
    else:
        minimum = num_3
    return minimum


def main():
    num_1 = int(input("Enter the first number: "))
    num_2 = int(input("Enter the second number: "))
    num_3 = int(input("Enter the third number: "))
    maximum, minimum = max_val(num_1, num_2, num_3)
    print("The minimum value is:", minimum, "and the maximum value is:", maximum)


main()
