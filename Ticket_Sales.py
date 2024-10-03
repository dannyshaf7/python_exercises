##########################################################################
# Create a program in Python that uses a loop for buying tickets to the  #
# Atlanta Falcons  --  General = 25.00 -- First row = 569.36             #
# Second Floor = 156.96 -- Tax = 0.08                                    #
# Ask the user which ticket they want to buy and how many they want      #
##########################################################################

def menu():
    print("1. General Admission - $25.00")
    print("2. First Row Admission - $596.36")
    print("3. Second Floor Admission - $156.96")
    print("")


def sub_total(type_ticket, num_ticket):
    while 1 <= type_ticket <= 3:
        if type_ticket == 1:
            return num_ticket * 25
        elif type_ticket == 2:
            return num_ticket * 569.36
        elif type_ticket == 3:
            return num_ticket * 156.96


def main():
    print("Welcome to the Atlanta Falcons Ticket Purchasing Program. Type 'exit' to quit.\n")
    menu_flag = True
    while menu_flag:
        menu()
        type_ticket = input("Which tickets do you want to buy (Options 1-3)? ")
        if type_ticket.lower() == "exit":
            menu_flag = False
        elif type_ticket.isdigit() and 1 <= int(type_ticket) <= 3:
            type_ticket = int(type_ticket)
            num_ticket = input("How many tickets would you like? ")
            if num_ticket.lower() == "exit":
                menu_flag = False
            elif num_ticket.isdigit() and int(num_ticket) > 0:
                num_ticket = int(num_ticket)
                taxes = sub_total(type_ticket, num_ticket) * 0.08
                total = round(sub_total(type_ticket, num_ticket) + taxes, 2)
                print("Your total ticket price is: ", total)
                print("")
            else:
                print("Invalid entry. Please try again.\n")
        else:
            print("Invalid entry. Please try again.\n")


main()
