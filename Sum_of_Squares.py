# Create a program in Python that gives the sum of the squares of N number
# chosen by the user
# Example: Input = 5; 1^2+2^2+3^2+4^2+5^2 = 55;
# Program has to have a function and a Loop


def sum_of_squares(number):
    total = 0
    for i in range(number + 1):
        square = i ** 2
        total += square
    return total


n = int(input("Enter a number. The calculator will square and then sum each number smaller than or equal."))
print(sum_of_squares(n), "\n")


# Alternative
def square(x):
    x = x + 1        # 1 has to be added in order to include the entered number in range
    num2 = 0       # the variable has to be defined before running the loop
    for i in range(1, x):
        num1 = pow(i, 2)
        num2 = num1 + num2
    print("your sum is:", num2)  # when print() is outside loop it will show result


def main():
    m = int(input("enter the number to find the sum of squares: "))
    square(m)


main()
