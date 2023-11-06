
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

# creating sample csv values
create_csv = ':'.join(['Makgabo','38','Tshwane University of Technology','Software Development'])
print('CSV Data Sample')
print( create_csv)



"""
Hey!

Reading and writing CSV files can be as simple as shown in the last couple lectures.

However, there can also be some problems. For example, if the data you're trying to save contains a comma (,) inside it, you could run into some trouble.

In addition, there are some performance improvements we can make, as well as make the code a little bit simpler.

We can do all that by using the built-in csv module. Nothing to install, just a couple lines of code that make everything better.

I've recorded a YouTube video explaining how the module works. It's not directly tied to this course's content, but I'm sure you won't have a problem understand everything I talk about in the video.

Check it out: https://www.youtube.com/watch?v=W7QByFjVom8

Happy coding!

Jose
"""