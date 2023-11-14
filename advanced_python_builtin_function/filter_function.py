
# filter function takes the function as the first argument, second argument being iterable

def starts_with_r(friend):
    return friend.startswith('R')


friends = ['Rolf', 'Jose', 'Randy', 'Anna', 'Mary']
starts_with = filter(starts_with_r, friends)

print("best solution is using the list instead of next")
print(list(starts_with))
"""print(next( starts_with ))
print(next( starts_with ))
print(next( starts_with ))
"""

cars = ['Volvo', 'Volkswage', 'BMW', 'Mercedez Benz', 'Porsche', 'Ferarri', 'Toyota', 'Suzuki', 'Hyundai', 'Isuzu', 'Mazda'
        'Audi', 'Ford', 'Alfa Romeo', 'Omoda', 'Opel', 'Beijing', 'Maseratti']

print('Using filter method with lambda function')
start_with_m = filter( lambda car: car.startswith('M'), cars)
another_starts_b = ( c for c in cars if c.startswith('B') )
print( list(another_starts_b) )
print( list(start_with_m) )

print(" the 'map' function")
cars_lower = map(lambda c:c.lower(), cars ) # this also returns an iterable
print(list(cars_lower))

