#######################################################
# 9/26/19 Daniel Shafer IP 3 Practice                 #
# Write a program that takes the plastic ID#          #
# from the user and returns information. All          #
# code should be in a function. Suggested Structure:  #
# printWelcome - prints program info                  #
# main - takes user input and returns the appropriate #
# information according to the chart in Word          #
#######################################################

def print_welcome():
    print("Welcome to the Plastic Information Application\n"
          "When prompted, enter the Plastic Identification number.\n"
          "The details of the type of plastic will be shown.\n")


def main():
    print_welcome()
    x = 0
    while x == 0:
        id_number = input("Please enter the Plastic Identification Number: ")
        if id_number.isdigit():
            id_number = int(id_number)
            if id_number == 1:
                print(
                    "1 – PET is intended for single use. Reusing increases the risk of carcinogen leaching and "
                    "bacterial growth. PET is difficult to decontaminate. Recycle but don’t reuse.")
                x = 1
            elif id_number == 2:
                print(
                    "2 – HDPE is one of the safest forms of plastic. Resistant to heat and cold. Can be reused and "
                    "recycled.")
                x = 1
            elif id_number == 3:
                print(
                    "3 – PVC is relatively impervious to sunlight and weather. It contains numerous toxins that can "
                    "leach throughout the lifecycle of the plastic. Cannot be recycled. Can be reused.")
                x = 1
            elif id_number == 4:
                print("4 – LDPE is relatively safe for use. Reusable but not always recyclable.")
                x = 1
            elif id_number == 5:
                print(
                    "5 – PP is heat-resistant and acts as a barrier against moisture, grease, and chemicals. Can be "
                    "reused and recycled.")
                x = 1
            elif id_number == 6:
                print(
                    "6 – PS is inexpensive and lightweight. Leaches carcinogens and breaks up easily. Low market for "
                    "recycling and difficult to reuse. Should be avoided.")
                x = 1
            elif id_number == 7:
                print(
                    "7 – PC and “other” plastics. These vary which is confusing for consumers. Because of concerns "
                    "with carcinogen leaching, avoid these unless it also contains the letters PLA or Compostable. "
                    "These are made from bio-based polymers that can be composted.")
                x = 1
            else:
                print("That is not a valid ID number! Please use options 1-7.")
        else:
            print("That is not a valid entry! Please enter only numbers.\n")


main()
