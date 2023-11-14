# generators in python
# what is generator: it is function that remembers the multiple states it has seen during its execution
# you can a generator multiple times, it will remember what it did the last time you ran it
from class_generators_iterators import FirstHundredNumbers
# an example of the code
def hundred_numbers():
    nums = []
    i = 0
    while i < 100:
        nums.append(i)
        i += 1
    return nums

# example of generator function:
def thousand_numbers():
    i = 0
    while i < 1000:
        yield i
        i += 1

print("Calling the function")
print( hundred_numbers())

print("Calling Generator function")
# first create a variable of the data type of the function
g = thousand_numbers()
print("# first call")
print( next(g) )

print("# second call")
print( next(g) )

print("# Get the remaining list of numbers from the generator since the last execution")

print(list(g))
# executing class from import
glGenerator = FirstHundredNumbers()
print("# executing class from import")
print( next( glGenerator ))
print( next( glGenerator ))




















