# Example 2: Create a program in Python that asks the user to specify a temp
# in one unit of measurement and gives the temp in a different unit of measure


def convert_fahrenheit(temp_f):
    temp_c = round((temp_f - 32) * 5/9)
    print("The temperature (rounded) in Celsius is: ", temp_c, "degrees.")


def convert_celsius(temp_c):
    temp_f = round((temp_c * 9/5) + 32)
    print("The temperature (rounded) in Fahrenheit is: ", temp_f, "degrees.")


def main():
    scale = input("What scale is your temperature in (type f for Fahrenheit, c for Celsius): ").lower()
    temp = float(input("Please enter the temperature to convert: "))
    if scale == "f":
        convert_fahrenheit(temp)
    elif scale == "c":
        convert_celsius(temp)


main()
