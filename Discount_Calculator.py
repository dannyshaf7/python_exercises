# Create a program in Python that find the total of a purchase of 10 articles.
# If the total is less than 25 dollars take 5% off from the total. If it is
# between 26 and 75 dollars take 10% and if more than 76 dollars take 20%.
# Remember to add the 8% sales tax after the discount and give the user the
# amount to pay.


def discount_calc(total_price):
    if total_price >= 75:
        discount = 0.20
        total_price = round(total_price-(total_price * discount), 2)
    elif total_price >= 25:
        discount = 0.10
        total_price = round(total_price-(total_price * discount), 2)
    else:
        discount = 0.05
        total_price = round(total_price - (total_price * 0.05), 2)
    discount = str(discount * 100)
    print("Your Discount is " + discount + "%.")
    print("Your Subtotal is: ", total_price)

    with_tax = round(total_price + (total_price * 0.08), 2)
    print("Your Total with Tax is: ", with_tax)


x = 0
total = 0
for x in range(10):
    item_number = str(x + 1)
    item_price = float(input("Enter the price of the item " + item_number + ": "))
    total += item_price

discount_calc(total)
