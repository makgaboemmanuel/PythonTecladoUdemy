
# filter function takes the function as the first argument, second argument being iterable

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def from_dict(cls, data):
        return cls(data['username'], data['password'])



def starts_with_r(friend):
    return friend.startswith('R')


friends = ['Rolf', 'Jose', 'Randy', 'Anna', 'Mary']
starts_with = filter(starts_with_r, friends)

print("best solution is using the list instead of next")
print(list(starts_with))
"""print(next( starts_with ))
print(next( starts_with ))
print(next( starts_with ))
"""

cars = ['Volvo', 'Volkswage', 'BMW', 'Mercedez Benz', 'Porsche', 'Ferarri', 'Toyota', 'Suzuki', 'Hyundai', 'Isuzu', 'Mazda'
        'Audi', 'Ford', 'Alfa Romeo', 'Omoda', 'Opel', 'Beijing', 'Maseratti']

print('Using filter method with lambda function')
start_with_m = filter( lambda car: car.startswith('M'), cars)
another_starts_b = ( c for c in cars if c.startswith('B') )
print( list(another_starts_b) )
print( list(start_with_m) )

print(" the 'map' function")
cars_lower = map(lambda c:c.lower(), cars ) # this also returns an iterable
print(list(cars_lower))

# using the User class
users = [
    { 'username': 'rolf', 'password': '113'},
    { 'username': 'tecladoisawesome', 'password': 'youaretoo'}
]

users = [User.from_dict(user) for user in users]
users = map(User.from_dict, users)


print("data  dictionary  users")

# please use video lesson 127 - any() and all() - this will also teach you about truthy values
# examples of truthy values -

"""
    0
    0.0
    None
    Null
    [] - empty list 
    () - empty map
    {} - empty data dictionary   
"""

"""
for key, value in users.items():
    print(key, "->", value)


for key, value in b_friends.items():
    print(key, "->", value)
"""