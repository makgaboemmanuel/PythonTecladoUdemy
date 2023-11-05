
# reading a CVS file
my_file = open("csv_read.csv", "r")
file_lines = my_file.readlines()
# shortcut to reading lines
simple_lines = [line.strip() for line in file_lines[1:]]

the_data = []
for aline in file_lines:
    the_data.append(aline)
    line_data = aline.split(",")
    print(aline, line_data[2])

# traversing the list: name,age,university,degree
get_name = []
get_age = []
get_university = []
get_degree = []
for all_d in the_data:
    line_data = all_d.split(",")
    get_name.append(line_data[0].capitalize()) # capitalise: will capitalise the first character in a string
    get_age.append(line_data[1])
    get_university.append(line_data[2].title()) # title: the first letter
    get_degree.append(line_data[3].upper()) # upper: will capitalize all characters in a string
print("List of All Names")
mm_name = [ a.strip() for a in get_name[1:]] # omitting the first item
print( mm_name ) # [line.strip() for line in file_lines[1:]]

print("List of All Age")
print( get_age )

print("List of All University")
print( get_university )

print("List of All Degrees")
print( get_degree )

# close the file
my_file.close()

# example of substring python
print("example of substring python ")
string = "freeCodeCamp"
print(string[0:5])
