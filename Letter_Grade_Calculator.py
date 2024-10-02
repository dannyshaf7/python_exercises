# Write a program w/a function and a condition that asks a user
# their GPA in number (2 decimals) and outputs a letter grade: A=3.5-4.0;
# B=2.5-3.49; C=1.60-2.49; Less than 1.60 did not pass

def letter_grade():
    if gpa >= 3.50:
        print("Your letter grade is A")
    elif gpa >= 2.50:
        print("Your letter grade is B")
    elif gpa >= 1.60:
        print("Your letter grade is C")
    else:
        print("You did not pass")


gpa = float(input("Please enter your GPA (rounded to 2 decimal places): "))
letter_grade()
