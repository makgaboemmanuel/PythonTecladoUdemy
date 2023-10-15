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
b_friends = { "name": "Rolf", "age": 24, "name": "Fred", "age": 41, "name": "Shamus", "age": 38, "name": "Kirk", "age":56, "name": "Max", "age": 29, "name": "Shane", "age": 40, "name": "Franklin", "age":40, "name": "Simon", "age": 30,  "name": "Lupita", "age": 55 }
friends = { "Rolf": 24, "Fred": 41, "Shamus": 38, "Kirk":56, "Max": 29, "Shane": 40, "Franklin": 40, "Simon": 30,  "Lupita": 55 }

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
time_since_seen = [ 3, 7, 15, 11]

long_timers = list(zip(c_friends,time_since_seen)) # list is using for casting
print(long_timers)

print("Enumeration in lists")
d_friends = ["Rolf", "Bob", "Jenny", "Anne"]
for counter, dd_friends in enumerate(d_friends):
    print(counter, dd_friends, sep="-")

print( list( enumerate(d_friends)) ) # converts to a list
print( dict( enumerate(d_friends)) ) # converts to a dictionary



