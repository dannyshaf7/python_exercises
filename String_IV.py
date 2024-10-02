# Example 4: Write Python code to request either "yes" or "no" from the user. Continue
# to prompt the user until either "yes" or "no" is entered. Then display their response

def check_input():
    word = input("Please enter yes or no: ").lower()
    x = 0
    while x == 0:
        if word == "yes" or word == "no":
            print(word)
            x = 1
        else:
            word = input("Unacceptable response, please enter yes or no: ").lower()


def main():
    check_input()


main()
