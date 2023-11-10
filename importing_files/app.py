import file_operations
from Garage import Garage  # second way of importing modules. you import only a specific section of the module

# this is called importing a module or execting the other file in module mode

# example of code calling from the other module
file_operations.save_to_file("Makgabo Emmanuel Mathekga","module_examples.txt")

# for context, you will multiple modules that you will import into a script
# [ the script is your main executable ]

my_garage = Garage() # creating an instance of the class
print("Getting the list of cars from the Garage object")
print(my_garage.cars)
my_garage.cars.append("Chrysler 300")
print(my_garage.cars)
