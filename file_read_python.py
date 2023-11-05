# opening a file
my_file = open("data.txt", "r")
file_content = my_file.read()
print("File Contents")
print(file_content)

my_file.close()

# creating a new file for writing
my_file_write = open("write_file.txt", "w")
my_file_write.write("Master Data Management | ETL | Business Intelligence")
my_file_write.close()
