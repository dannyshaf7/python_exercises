# Write a fn that takes the weight in kg and returns the weight in pounds
# 1kg = 2.205 lbs

def convert_kg(x):
    return x * 2.205


kg = float(input("Enter your weight in kilograms: "))
print("Your weight in pounds is", convert_kg(kg))
