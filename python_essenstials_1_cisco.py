# course URL: https://skillsforall.com/course/python-essentials-1?courseLang=en-US
print("Question 1")
my_list = [1, 2]
for v in range(2):
    my_list.insert(-1,my_list[v])
my_list[v]
print(my_list)

print("Question 2")
nums =[1, 2, 3]
vals = nums
print(nums)
print(vals)

print("Question 2")
def function_1(a):
    return None

def function_2(a):
    return function_1(a) * function_1(a)
#print(function_2(2)) : TypeError: unsupported operand type(s) for *: 'NoneType' and 'NoneType'

print("Question 3")
print(1//2)

print("Question 4")
def func(a, b):
    return b ** a
# print(func(b=2, 2)) : SyntaxError: positional argument follows keyword argument

print("Question 4")
z = 0
y = 10
x = y < z and z > y or y < z and z < y
print("Value of x: ",x)

print("Question 5")
a_list = [x * x for x in range(5)]

def fun(lst):
    del lst[lst[2]]
    return lst
print(fun(a_list))

x = 1
y = 2
x, y, z = x, x, y
z, y, z = x, y, z
print("Question 6")
print(x, y, z)

print("Question 7")
a = 1
b = 0
a = a ^ b
b = a ^ b
a = a ^ b
print(a, b)

print("Question 8")
def fun(x):
    if x % 2 == 0:
        return 1
    else:
        return 2
print(fun(fun(2)))

print("Question 9")
nums = [1, 2, 3]
vals = nums
del vals[:]
print(nums)
print(vals)

print("Question 10")
"""# x = int(input())
# y = int(input())
x = x % y
x = x % y
y = y % x
# print(y) """

print("Question 11")
""" y = input()
x = input()
print(x+y) """

print("Question 12")
print("a", "b", "c", sep="sep")

print("Question 13")
x = 1 // 5 + 1 / 5
print(x)

print("Calling Self Calling Function - 8th")
my_turple = {1, 4, 8, 3}
# my_turple[1] = my_turple[1] + my_turple[0] : Ty peError: 'set' object is not subscriptable

print("Question 13")
x = float(input())
y = float(input())
print(y ** (1 / x))
# print("y value: ",y)

print("Question 14")
dictionary = {'one': 'two',
              'three': 'one',
              'two': 'three'}
v = dictionary['three']

for k in range(len(dictionary)):
    v = dictionary[v]
print(v)


print("Question 15")
lst = [ i for i in range(-1, -2)]
print(len(lst))

print("Question 16")
def fun(x, y):
    if x == y:
        return x
    else:
        return fun(x, y -1)
print(fun(0, 3))

print("Question 17")
i = 0
""" while i < i + 2:
    i += 1
    print("*")
else:
    print("*")"""

print("Question 18")
tup = (1, 2, 4, 8)
tup = tup[-2:-1]
tup = tup[-1]
print(tup)

print("Question 19")
dd = {"1": "0", "0":"1"}
""" for x in dd.vals():
    print(x, end="") """

print("Question 20")
dct = {}
dct[1] = (1, 2)
dct[2] = (2, 1)

for x in dct.keys():
    print(dct[x][1], end="")

print("")
print("Question 21")
def fx(inp=2,out=3):
    return inp * out

print(fx(out=2))

print("Question 22")

lst = [[x for x in range(3)] for y in range(3)]

for r in range(3):
    for c in range(3):
        if lst[r][c] % 2 != 0:
            print("#")

print("Question 22")
try:
    value = input("Enter a value:")
    print( int(value) / len(value))
except ValueError:
    print("Bad input...")
except ZeroDivisionError:
    print("Very bad input")
except TypeError:
    print("Very very bad input...")
except:
    print("Booo!")

print("Question 23")
try:
    print(5/0)
except (ValueError, ZeroDivisionError):
    print("Too bad...")
# except:
  #  print("Sorry, something went wrong...")

print("Question 24")
foo = (1, 2, 3)
#print(foo.index(0))
# print(Hello World)
