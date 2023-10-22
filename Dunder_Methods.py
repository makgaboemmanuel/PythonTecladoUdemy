""""
What are dunder methods in python
ChatGPT
Dunder methods in Python are special methods with double underscores at the beginning and end of their names.
They are also known as "magic methods" or "special methods." Dunder stands for "double underscore."
These methods are used to define how objects of a class behave in various operations and interactions, making it
possible to customize the behavior of built-in operators and functions. Dunder methods are an integral part of Python's
object-oriented programming and enable you to create user-defined classes that emulate the behavior of built-in data types.

Here are some common dunder methods and their purposes:

__init__: This method is called when an object of the class is created. It initializes the object's attributes.

__str__: Used to define a human-readable string representation of the object when str() or print() is called on it.

__repr__: Defines an unambiguous string representation of the object for debugging purposes. It is used when repr() is called on the object.

__len__: Allows you to define the length of an object using the len() function.

__getitem__ and __setitem__: These methods are used for indexing and item assignment, respectively, to make objects
behave like sequences (e.g., lists or dictionaries).

__iter__ and __next__: These methods allow objects to be iterable, making it possible to use them in for loops.

__add__, __sub__, __mul__, and other mathematical operators:
These methods enable you to define custom behavior for mathematical operations on objects.

__eq__, __ne__, __lt__, __le__, __gt__, and __ge__: These methods allow you to customize comparison operations (e.g.,
equality and ordering) for objects.

__call__: Allows an object to be callable like a function.

__enter__ and __exit__: Used in context management with the with statement to define setup and teardown operations.

Dunder methods provide a way to define the fundamental behavior of your custom objects and allow them to seamlessly
integrate with Python's built-in functions and operators. By implementing these methods, you can create classes that
behave like native data types, enhancing the expressiveness and flexibility of your code.

"""