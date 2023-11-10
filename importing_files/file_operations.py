# first method
# writing to a file
def save_to_file(content, filename):
    with open(filename, "w") as file:
        file.write(content)

# second method
# read from a file
def read_file(filename):
    with open(filename, "r") as file:
        return file.read()


