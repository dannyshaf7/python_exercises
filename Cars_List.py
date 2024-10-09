# create and print list of cars
# remove all cars that start with letter F
# add back one of the car brands


def main():
    cars= ["Acura","BMW","Chevy","Dodge","Ferrari","Ford","GMC","Honda","Infinity","Lincoln","Mercedes",
           "Nissan","Toyota","Volvo","Zonda"]
    print("List of car brands: \n", cars)
    for x in cars:
        print(x, end="")
    print("\nRemoving car brands that start with F... \n")
    cars = [x for x in cars if not x.startswith("F")]

    print("List of car brands that don't start with F: \n", cars)
    for x in cars:
        print(x, end="")
    print("\nAdding only Ferrari back to list... \n")
    cars.append("Ferrari")
    cars.sort()
    print("List of car brands: \n", cars)
    for x in cars:
        print(x, end="")


main()
