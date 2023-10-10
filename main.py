# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# course URL: https://blts.udemy.com/course/the-complete-python-course/learn/lecture/9412506#overview

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    age = 35
    name = 'Makgabo Emmanuel Mathekga'
    print('Dealing With Variables')
    print(name, age)

    # variables in capital letters are considered constants and should not be changed
    PI = 3.14
    PI = PI * 2
    print('PI value is:', PI)

    RADIANS_DEGREES = 180 / PI

    # important note, when you do a division in python, the returned data type is a float. even if there is no remainder
    # to avoid the comma after the division, use // , the second division sign removes the comma
    # this only works if there is no remainder

    print('Float value after division: ', RADIANS_DEGREES)
    print('Float value after division: ', 10 / 5)
    print('Integer value after division: ', 10 // 5)
    # See PyCharm help at https://www.jetbrains.com/help/pycharm/

    # remainder in Python - uses the modulus % operator
    modulus_example = 6 % 5
    print('Remainder example: ', modulus_example)
    # using the modulus operator to determine the odd and even numbers
    odd_even = 2 % 2
    if odd_even != 0:
        print('Not an even number')
    else:
        print('It is an even number')

    # use double quotes if you have single quotes inside the string.
    # otherwise escape the character to ensure the quote is part of the value if the string
    string_ex = "Makgabo\' Emmanuel Mathekga"

    print('String example: ', string_ex)

    # multi-line strings: you must use triple string quotes at beginning and end
    newspaper = """Bomma ke boss
    O fetsa puff
    Idibala
    Ke gopotse ex yaka 
    """
    print(newspaper)
    final_greeting = "Good day {person}"
    my_greeting = final_greeting.format(person=string_ex)
    print(my_greeting)

    # you can also use multi line strings as comments without the variable name
    """"
        this is a comment
        and won't be used anywhere in the code
        if you have long text that you want to write
    """
    # dealing with user input

    print("Please provide your name")
    none = "I forgot my name"
    my_name = input()
    exact_name = my_name or none # this is an example of truthy values
    print(f"Your name is {exact_name}")
    # important:
    # int * int = int
    # float * int = float
    # string * int = string will be printed the number of int times
    print(f"You are {6 * 'd'} months old")
    # converting: input always returns a string data type, you have to explictly convert it to any other format
    print("Please provide your salary")
    salary = int(input())
    print(f"Your salary is {salary}")  # .format(salary)

    # comparison statements in Python:
    print(f"Using comparison statements: 5 > 3: ", (5 > 3))
    # == compares the equality of two values
    print(f"Using comparison statements: 5 == 3: ", (5 == 3))

    # dealing with and as well as or
    results = salary < 65 and len(my_name) > 10
    print("Using and as wel as or:", results)
    # bool function in Python, checks if a value is true or not. return true as long as the value is not empty
    print(bool("Makgabo"))
    print(bool(""))  # False because the value being checked is empty
    print(bool(0))  # False because the value being checked is 0

    """
    Therefore, whenever we refer to an “array,” we mean a “NumPy array.” Lists are another data structure, similar to NumPy arrays, but unlike NumPy arrays, 
    lists are a part of core Python. Lists have a variety of uses. They are useful, for example, in various bookkeeping tasks that arise in computer programming.
    """

    fruits = ["Pear", "Orange", "Apple", "Guava"]
    print("Iterating fruits list. Size of the list: ", len(fruits))
    for fruit in fruits:
        print(fruit)

    # accessing a specific element of the list
    print("Acessing last element of the list: ", fruits[ len(fruits) -1])
    # dealing with 2-dimensional lists
    people_ages = [
        ["Makgabo", 33],
        ["Emmanuel", 40],
        ["Frank", 66],
        ["Paul", 51],
        ["Alex", 68],
    ]
    print("Accessing 2-dimensional lists values", people_ages[0][1])
    for a in people_ages:
        c = ""
        for b in a:
            c = c + " " + str(b)
        print(c)

    # using a for loop a counter variables
    print("# using a for loop a counter variables")
    for i in range(len(fruits)):
        print( fruits[i])

    fruits.remove("Orange")
    print(fruits)

    print("# Dealing with Tuples")
    ex_tuple = "Volkwagen", "Jeep", "Peugeot"
    print(len( ex_tuple ))
    print("# Appending values to a Tuples")
    ex_tuple = ex_tuple + ("Hyundai, Ford",)
    for ex_tp in ex_tuple:
        print(ex_tp)

    print("# Dealing with Sets - doesn't allow duplicates")
    art_friends = { "Thomas", "Erling", "Pearl", "Caiphus"} # "Thomas",
    sci_friends = {"Jen", "Charlie", "Chuck", "Owen", "Billy", "Caiphus", "Thomas"}
    print(art_friends)
    art_friends.add("Pearl") # adding a new element to the set
    print(art_friends)
    # art_friends.remove("Thomas") # removing an element from the set
    print(art_friends)
    #

    print("Default Values: 'art_friends' ",art_friends)
    print("Default Values:  'sci_friends' ",sci_friends)
    print("Non-Common Friends")
    print(sci_friends.difference(art_friends)) # finds the elements that are in sci_friends but not in art_friends
    print(art_friends.difference(sci_friends))  # finds the elements that are in art_friends but not in sci_friends

    # symmetric differences: symmetric_differences
    print("Symmetric Differences: ",art_friends.symmetric_difference(sci_friends))
    print("Common Elements", art_friends.intersection(sci_friends))


