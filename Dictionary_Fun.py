# basic dictionary operation

my_dict={
    "date": "2019",
    "course": "Python",
    "grades": "passing",
    "logo": "Happy Ending"}

print("My Basic Dictionary: \n" + str(my_dict))  # prints dictionary as a string
print("Logo: ", my_dict["logo"]) # prints the value under "logo" in the dictionary
my_dict["date"] = 1964 # changes the value under "date" in the dictionary
print(my_dict)         # reprints dictionary as a list with new value
print(*my_dict.keys(), sep=", ")  #prints only the keys, separated by commas

# Create a Dictionary for kids, seniors, young adults, and adults.
# Give value the range for each age. Print your dictionary

ages_dict={
    "kids": "0-17",
    "young adults": "18-35",
    "adults": "36-64",
    "seniors": "65+", }

print("\nAges Dictionary: \n" + str(ages_dict))



def print_person_info(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")

person = {"age": 30, "name": "Alice", "city": "New York"}

# Unpacking the dictionary into the function
print_person_info(**person)  # Output: Name: Alice, Age: 30, City: New York