##############################################################################
# Let's try a factorial problem. To calculate the factorial of a non-negative#
# integer x, just multiply all the integers from 1 through x. For example:   #
# 3! is equal to 6!                                                          #
##############################################################################


def factorial(x):
    count = 1
    for i in range(x):
        count = count * (i + 1)
    return count


n = input("enter a number to find the factorial: ")
n = int(n)
factorial(n)
print("your factorial result is: ")
print(factorial(n))
