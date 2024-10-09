# Using the following message program python to print the following:
#   1. How many a are in the message
#   2. Find the position of Hay
#   3. find the length of the message
#   4. introduce your name at the beginning
#   5. print the characters between 5 and 10
#   6. Change the Character at 14 to P

# Relax and enjoy life
# Know that whatever you need to know is revealed to you in the perfect
# time and space sequence
# Louise L. Hay

message = """{} Relax and enjoy life.
Know that whatever you need to know is revealed
to you in the perfect time and space sequence.
Louise L. Hay"""

print(message[3:], "\n")
print("Message Count: ", message.count("a"))
print("Location of Hay in Message: ", message.find("Hay"))
print("Length of Message: ", len(message))
message_edit = message.format("Daniel,")
print("Personalized Message: ", message_edit)
print("Characters between location 5 and 10: ", message[5:10])
message_edit = message_edit[0:14] + "P" + message_edit[15:]
print("Message with Character at location 14 changed to P: ", message_edit)

# New version of formatting with f
name = input("\nEnter your name: ")
age = input("Enter your age: ")
m1= f'Your name is {name} and your age is {age}'
m2= 'Your name is {} and your age is {}'.format(name,age)
print(m1)
print(m2)