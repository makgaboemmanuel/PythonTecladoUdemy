# Define a PrimeGenerator class
class PrimeGenerator:
    # You may modify the __init__() method if necessary, but you don't need to change its arguments
    def __init__(self, stop):
        self.stop = stop  # stop defines the range (exclusive upper bound) in which we search for the primes

    def __next__(self):
        i = 0
        if i <= self.stop:
            current = i
            i += 1
            if current % 2 != 0:
                return current
        else:
            raise StopIteration

"""
class PrimeGenerator:
    def __init__(self, stop):
        self.stop = stop
        self.start = 2
 
    def __next__(self):
        for n in range(self.start, self.stop):  # always search from current start (inclusive) to stop (exclusive)
            for x in range(2, n):
                if n % x == 0:      # not prime
                    break
            else:   # n is prime, because we've gone through the entire loop without having a non-prime situation
                self.start = n + 1  # next time we need to start from n + 1, otherwise we will be trapped on n
                return n    # return n for this round
        raise StopIteration()  # this is what tells Python we've reached 
"""

