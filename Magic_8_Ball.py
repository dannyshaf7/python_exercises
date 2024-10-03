# Write a function called answer that takes an integer as an argument (parameter)
# and returns one of 8 different responses based on the value of that integer.
# Write a main function that
#  a. Asks the user to enter a yes/no question
#  b. Generates a random number between 1 and 8
#  c. Calls the function answer() and provides the generated random number as the
#     given argument
#  d. Prints the response returned from the function answer() as the answer to the
#      user's question.
#  e. The program should take questions from the user and print response until
#     the user enters "quit"

# Sample Run:
# Hi and welcome to the magic 8-ball. Ask a yes or no question and get a response.
# When you are done asking questions, enter "quit"

import random


def answer(integer):
    if integer == 1:
        return "Yes\n"
    elif integer == 2:
        return "No\n"
    elif integer == 3:
        return "Maybe\n"
    elif integer == 4:
        return "Not so clear\n"
    elif integer == 5:
        return "Ask again later\n"
    elif integer == 6:
        return "Absolutely\n"
    elif integer == 7:
        return "Absolutely not\n"
    elif integer == 8:
        return "The number you have reached is currently out of service\n"


def main():
    print("Hi and welcome to the Magic 8 Ball.")
    print("Ask a yes  or no question and get a response!")
    print("When you are done asking questions, enter ""quit"" \n")
    question = True
    while question:
        question = input("Please enter your Yes or No question: ")
        if question.lower() == "quit":
            question = False
        else:
            print(answer(random.randint(1, 8)))
    print("Thanks for playing!!!")


main()
