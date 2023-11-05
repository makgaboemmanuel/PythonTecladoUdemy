# reading an input file
read_file = open("questions.txt", "r")
file_content = read_file.read().split("\n")
print("Type of Object:", type(file_content))

total = 0
result_tostore = []
for str in file_content:
    str_vals = str.split("=")
    print(f'What is result of: {str_vals[0]}')
    user_input = input()
    result_tostore.append(str_vals[0] + "=" + user_input)
    if( str_vals[1] == user_input):
        total = total + 1
    print("Value: ",str_vals[0])
    print("Result: ", str_vals[1])


print(f'Number f correct answers is: {total}')
file_write = open("results.txt", "w")
# writing content to a file
#for line in result_tostore:
    # file_write.write(line + "\n")
# file_write.write(result_tostore)
print(f"Your final score is: { total / len(file_content)}")
file_write.write(f"Your final score is: { total / len(file_content)}")
file_write.close()
read_file.close()