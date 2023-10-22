class Garage:
    def __init__(self):
        self.cars = []

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