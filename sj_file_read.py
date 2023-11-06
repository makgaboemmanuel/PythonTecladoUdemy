import json

file = open("json_file.txt", "r")
file_contents = json.load(file)
print( file_contents['friends'][0])
print("Size of Elements in the JSON: ", len( file_contents['friends']))
print("Please navigate the JSON")
count = 0
for friends in file_contents['friends']:
    record = file_contents['friends'][count]
    print(file_contents['friends'][count])

    print("Name of Dictionary: ", record["name"])

    count = count + 1

count = 0
file.close()

print("saving SJON Data" )
cars = [
    {
        'make': 'Ford',
        'model': 'Fiesta'
    },
{
        'make': 'Hyundai',
        'model': 'Santafe'
    }
]
file_write = open("cars_json.txt", "w")
json.dump(cars, file_write)
file_write.close()

