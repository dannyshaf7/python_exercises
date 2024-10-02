# Example 4: Create a program that asks the user their Zodiac sign and give them
# the month Switch (Select case) Aquarius Cancer, leo, capricorn, scorpio,
# sagitarius,pices, gemini, taurus, virgo, libra, aries


def zodiac_month(sign):
    match sign.lower():
        case "aries":
            print("You were born between March 21 and April 19")
        case "taurus":
            print("You were born between April 20 and May 20")
        case "gemini":
            print("You were born between May 21 and June 20")
        case "cancer":
            print("You were born between June 21 and July 22")
        case "leo":
            print("You were born between July 23 and August 22")
        case "virgo":
            print("You were born between August 23 and September 22")
        case "libra":
            print("You were born between September 23 and October 23")
        case "scorpio":
            print("You were born between October 24 and November 21")
        case "sagittarius":
            print("You were born between November 22 and December 21")
        case "capricorn":
            print("You were born between December 22 and January 19")
        case "aquarius":
            print("You were born between January 20 and February 18")
        case "pisces":
            print("You were born between February 19 and March 19")


sign = input("Please enter your Zodiac sign: ")
zodiac_month(sign)
