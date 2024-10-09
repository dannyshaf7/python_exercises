# From given list of gadgets:
#   a) create separate lists of strings and numbers
#   b) sort the strings list in ascending order
#   c) sort the strings list in descending order
#   d) sort the numbers list from lowest to highest

gadgets = ["Mobile", "Laptop", 100, "Camera", 310.28, "Speakers", 27.00, "Television", 1000, "Laptop Case", "Camera Lens"]
numbers = [x for x in gadgets if isinstance(x,int) or isinstance(x, float)]
strings = [x for x in gadgets if isinstance(x,str)]

print("Gadgets List: ", gadgets)
print("Numbers List: ", numbers)
print("Strings List: ", strings)
print("Strings List sorted in ascending order: ", sorted(strings))
print("Strings List sorted in descending order: ", sorted(strings, reverse=True))
print("Numbers Lis sorted from lowest to highest: ", sorted(numbers))

# From given list of scores:
#   a) Get first second best scores from the list.
#   b) List may contain duplicates, sort and remove duplicates.

scores= [86,86,85,85,85,85,83,23,45,84,1,2,0]
print("\nScores: ", scores)
scores.sort(reverse=True) # sorts in reverse of ascending order
print("Sorted Scores: ", scores)
scores= list(dict.fromkeys(scores)) # auto remove dupl, dict can't have dupl keys
print("Top 2 scores: ", scores[0], scores[1])