# Simple Interest Formula p*t*r/100
# p=principle, t=time in months, r=interest rate
# Create a program in Python that calculates the simple interest.
# The rate is 11.5%, the time is 5 years and the amount is 34500.

def interest(p, t, r):
    return p * t * r


principle = float(input("Please enter the amount borrowed in dollars: "))
time_of_loan = float(input("Please enter the length of the loan in years: "))
interest_rate = float(input("Please enter the percent interest: "))/100

print("Your total interest is", interest(principle, time_of_loan, interest_rate))
