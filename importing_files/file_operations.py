# first method
# writing to a file
def save_to_file(content, filename):
    # there are two / 2 modes of writing to a file,
    # w - means over-writing the existing content
    # a - means appending to the existing content
    with open(filename, "a") as file:
        file.write(content)

# second method
# read from a file
def read_file(filename):
    with open(filename, "r") as file:
        return file.read()


