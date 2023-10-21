import Student as Student
# importing a class, as student
lottery_numbers = {13, 21, 22, 5, 8}

"""
A player looks like this:

{
    'name': 'PLAYER_NAME',
    'numbers': {1, 2, 3, 4, 5}
}

Define a list with two players (you can come up with their names and numbers).
"""
players = [
    {
        "name": "Rolf",
        "numbers": {1, 3, 8, 22, 21}
    },
    {
        "name": "Jose",
        "numbers": {4, 9, 10, 12, 15}
    }
]

# For each of the two players, print out a string like this: "Player PLAYER_NAME got 3 numbers right.".
# Of course, replace PLAYER_NAME by their name, and the 3 by the amount of numbers they matched with lottery_numbers.
# You'll have to access each player's name and numbers, and calculate the intersection of their numbers with lottery_numbers.
# Then construct a string and print it out.

# Remember: the string must contain the player's name and the amount of numbers they got right!
name = players[0]["name"]
numbers = players[0]["numbers"].intersection(lottery_numbers)
print(f"Player {name} got {len(numbers)} numbers right.")

name = players[1]["name"]
numbers = players[1]["numbers"].intersection(lottery_numbers)
print(f"Player {name} got {len(numbers)} numbers right.")

user_input = input()

while user_input == 'p':
    if user_input == 'p':
        print('Hello')
    user_input = input()
    if user_input == 'q':
        break

# system provided solution:
# Ask the user to choose one of two options:
# if they type 'p', our program should print "Hello" and then ask the user again. Keep repeating this until...
# if they type 'q', our program should terminate.

# Let's begin by asking the user to type either 'p' or 'q':
user_input = input("Enter q or p: ")

# Now we must repeat until they type 'q':
while user_input != "q":
    # Inside our loop, check if they typed 'p'. If they did, print "Hello"
    if user_input == "p":
        print("Hello")
    # Now we must ask the user for their input again—otherwise we would be in an infinite loop!
    user_input = input("Enter q or p: ")

# iterating through dictionaries:
b_friends = {"name": "Rolf", "age": 24, "name": "Fred", "age": 41, "name": "Shamus", "age": 38, "name": "Kirk",
             "age": 56, "name": "Max", "age": 29, "name": "Shane", "age": 40, "name": "Franklin", "age": 40,
             "name": "Simon", "age": 30, "name": "Lupita", "age": 55}

print("Iterating named data dictionary")
for key, value in b_friends.items():
    print(key, "->", value)

friends = {"Rolf": 24, "Fred": 41, "Shamus": 38, "Kirk": 56, "Max": 29, "Shane": 40, "Franklin": 40, "Simon": 30,
           "Lupita": 55}

for key, value in friends.items():
    print(f"{key} is age {value} old")

for key in friends:
    print(key, friends[key], sep=" -- ")
print("Size of dictionary", len(friends))

for i in range(1, 101):
    if i % 3 == 0:
        print("Fizz")
    if i % 5 == 0:
        print("Buzz")
    if i % 3 == 0 and i % 5 == 0:
        print("Fizz")
    else:
        print(i)

print("Using the zip function in collections")
c_friends = ["Rolf", "Bob", "Jenny", "Anne"]
time_since_seen = [3, 7, 15, 11]

long_timers = list(zip(c_friends, time_since_seen))  # list is using for casting
print(long_timers)

print("Enumeration in lists")
d_friends = ["Rolf", "Bob", "Jenny", "Anne"]
for counter, dd_friends in enumerate(d_friends):
    print(counter, dd_friends, sep="-")

print(list(enumerate(d_friends)))  # converts to a list
print(dict(enumerate(d_friends)))  # converts to a dictionary

print("Example on Lists")
numbers = list(range(10))
doubled = [n * 2 for n in numbers]  # please understand the meaning of this code

print(numbers)
print(doubled)

print("Exercise practice - to Upper")
guests = ['Jose', 'Rolf', 'ruth', 'Charlie', 'michael']
new_guests = [names.upper() for names in guests]
print(new_guests)

print("What would be the best way to turn this list of tuples into a dictionary?")

guests = [('rolf', 25), ('adam', 28), ('jen', 24)]
turple_guests = dict(guests)
print(turple_guests)

# coding exercise 10: 19-10-2023
import random

# This line creates a set with 6 random numbers
lottery_numbers = set(random.sample(list(range(22)), 6))

# Here are your players; find out who has the most numbers matching lottery_numbers!
players = [
    {"name": "Rolf", "numbers": {1, 3, 5, 7, 9, 11}},
    {"name": "Charlie", "numbers": {2, 7, 9, 21, 10, 5}},
    {"name": "Anna", "numbers": {13, 14, 15, 16, 17, 18}},
    {"name": "Jen", "numbers": {19, 20, 12, 7, 3, 5}},
]

# Then, print out a line such as "Jen won 1000.".
# The winnings are calculated with the formula:
# 100 ** len(numbers_matched)

print("# coding exercise 10: 19-10-2023")
print(lottery_numbers)
# output: {0, 12, 15, 16, 18, 20}
# output: {2, 8, 9, 10, 11, 15}
concat = ""
print("Size of Players: ", len(players))
match_winner = None
highest_winner = 0
for player in players:
    matches = len(player["numbers"].intersection(lottery_numbers))

    if matches > highest_winner:
        highest_winner = matches
        winner = player

winnings = 100 ** highest_winner
if winner:
    print(f"{winner['name']} won {winnings}")
else:
    print("No one won this time")

print("Iterating Data Dictionary and Understanding")
my_student = {
    "name": "Ralph Smith",
    "grades": [70, 88, 90, 99]
}
all_names = my_student["name"]
all_grades = my_student["grades"]

print("Names: ", all_names)
print("Players: ", all_grades)

avg_grades = sum(all_grades) // len(all_grades)
print("Average grades are: ", avg_grades)


def get_avg_grades(astudent):
    return sum(astudent) // len(astudent)


print(get_avg_grades(all_grades), "Avg grades, Using Function")

class Person:
    def __init__(self, new_name, new_grades):
        self.new_name = new_name
        self.new_grades = new_grades

    def average(self):
        return sum(self.new_grades) // len(self.new_grades)

person_one = Person("Ralph Smith", [70, 88, 90, 99])
print("# calling from another class, syntax: filename.class_name")
student_one = Student.Student("Ralph Smith", [70, 88, 90, 99])
print("Calling a class method: ", student_one.average())

print()

# We've already defined a movie class like this:
class Movie:
    def __init__(self, new_name, new_director):
        self.name = new_name
        self.director = new_director

    # let's try to add a method `print_info()` here:

    def print_info(self):
        print(f"<<{self.name}>> by {self.director}")
# You only need to finish the method, we will take care of the object creation and call your method for you!
aamovie = Movie('The Matrix', 'Wachowski')
print("Using Movie Class ", aamovie.print_info())




""""
SOLUTION:
import random

# This line creates a set with 6 random numbers
lottery_numbers = set(random.sample(list(range(22)), 6))

# Here are your players; find out who has the most numbers matching lottery_numbers!
players = [
    {"name": "Rolf", "numbers": {1, 3, 5, 7, 9, 11}},
    {"name": "Charlie", "numbers": {2, 7, 9, 21, 10, 5}},
    {"name": "Anna", "numbers": {13, 14, 15, 16, 17, 18}},
    {"name": "Jen", "numbers": {19, 20, 12, 7, 3, 5}},
]

# Initialize variables to keep track of the winner and the highest number of matches
winner = None
highest_matches = 0

# Iterate through each player and check their numbers against the lottery_numbers
for player in players:
    matches = len(player["numbers"].intersection(lottery_numbers))
    
    if matches > highest_matches:
        highest_matches = matches
        winner = player

# Calculate the winnings
winnings = 100 ** highest_matches

# Print out the result
if winner:
    print(f"{winner['name']} won {winnings}.")
else:
    print("No one won this time.")

"""
