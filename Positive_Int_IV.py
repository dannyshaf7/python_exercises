##############################
# Example 1 Input Validation #
##############################

def check_input(number):
    x = True
    while x:
        if not number.isdigit() or int(number) < 0:
            print("that is not an expected value")
            number = input("enter a positive number: ")
        else:
            print("number accepted, subtracting by 20...\n")
            number = int(number) - 20
            print(number)
            x = False


def main():
    check_input(input("enter a positive number: "))


main()
