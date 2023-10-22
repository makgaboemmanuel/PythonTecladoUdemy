class Garage:
    def __init__(self):
        self.cars = []

    # defining the method to get the length of the element of the class
    def __len__(self):
        return len(self.cars)

    # method to return the value at certain index
    def __getitem__(self, i):
        return self.cars[i]

    # wrapper method - this is called the same way as the __str__ method
    def __repr__(self):
        return f'<Garage> {self.cars}'

    # returning the string version of the class / object - this is called the same way as the __str__ method
    """ def __str__(self):
        return f'Garage with {len(self.cars)} cars' """

# creating an instance of the class
ford = Garage()
print("List of cars for the object")
print(ford.cars)

# adding values to the list
my_cars = ["Mustang", "Fiesta", "Puma", "Everest", "Ranger", "Focus", "Fusion"]

for i in my_cars:
    ford.cars.append(i)

print("Getting Values of The List")
print(ford.cars)
print(len(ford), " - Getting the length of the cars property")
print(ford[3], " - Getting an item at an index")
print(ford, " - String version of te Garage Object") # currently, it is calling the wrapper method since the string method is disabled





