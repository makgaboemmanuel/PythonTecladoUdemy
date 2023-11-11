import file_operations
from Garage import Garage  # second way of importing modules. you import only a specific section of the module
from file_operations import save_to_file, read_file # importing specific methods from the included class
from file_dest.data_source import sort_list # if it is grey, it means it isn't used at all
# in order to import files in a different folder
# you must use the syntaxt: folder_name.file_name without the extension of course

# this is called importing a module or execting the other file in module mode

# example of code calling from the other module
file_operations.save_to_file("Makgabo Emmanuel Mathekga\n","module_examples.txt")

# for context, you will multiple modules that you will import into a script
# [ the script is your main executable ]

my_garage = Garage() # creating an instance of the class

print("Getting the list of cars from the Garage object")

print(my_garage.cars)
my_garage.cars.append("Tiggo Pro 8")
my_garage.cars.append("Mini Cooper S")
my_garage.cars.append("Chrysler 300")

print("Un-Sorted List")
print(my_garage.cars)

print("using or calling the read_file")

print(read_file("module_examples.txt"))

# using a file from another directory
print("Sorted List")


def sort_lists(my_list):
    return my_list.sort()

test_list = ["Tiggo Pro 8","Mini Cooper S", "Chrysler 300"]
print( sort_lists(test_list)) # please check this as it is  not working




