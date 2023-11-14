
# example class solution
class FirstHundredNumbers:
    def __init__(self):
        self.number = 0

    def __next__(self):
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration

# what are iterables - classes that implement the method __iter__


class FirstHundredIterable:
    def __iter__(self):
        return FirstHundredNumbers()

# executing the class
glGenerator = FirstHundredNumbers()
print("# executing class from import")
print( next( glGenerator ))
print( next( glGenerator ))

print(" using the iterable class ")
print( sum(FirstHundredIterable()) )

print("# using the class to iterate")

for i in FirstHundredIterable():
    print(i)

# new class on iterable
class AnotherIterable:
    def __init__(self):
        self.cars = ['Fiesta', 'Focus']

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, i):
        return self.cars[i]

print("using the newly created class")
for i in AnotherIterable():
    print(i)
