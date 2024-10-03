# Write a fn that takes the height in meters and returns the height in inches
# 1 m = 39.37 in

def convert_m(x):
    return x * 39.37


m = float(input("Enter your height in meters: "))
print("Your height in inches is", convert_m(m))
