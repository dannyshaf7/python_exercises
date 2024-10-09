# create a program that prompts a user to enter a number between
# 50 and 100. Check whether a valid number was entered, if not
# print error message and if so check whether number is in a
# more specific range 50-74 or 75-100 and print an accept message
# or reject message respectively


def user_validation(number):
    if number < 50 or number > 100:
        return False
    else:
        return True


def print_answer(number):
    if 50 <= number < 75:
        print("Thank you for your interest in our program!")
    elif 75 <= number <= 100:
        print("Good bye, see you another time!")


def main():
    number = 1
    while number != 0:
        try:
            number = int(input("Enter a number between 50 and 100 (enter 0 to exit): "))
            if number == 0:
                return
            elif user_validation(number):
                print_answer(number)
                print("")
            else:
                print("Number out of range.")
                print("")
        except ValueError:
            print("Not a number, please try again.")


main()
