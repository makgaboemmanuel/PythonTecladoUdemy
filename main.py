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

    # you can also use multi line strings as comments without the variable name
    """"
        this is a comment
        and won't be used anywhere in the code
        if you have long text that you want to write
    """

