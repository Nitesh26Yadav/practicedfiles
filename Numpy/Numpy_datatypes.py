'''
---------------------------------- Data Types in Python ----------------------------------
By default Python have these data types:

# strings - used to represent text data, the text is given under quote marks. e.g. "ABCD"
# integer - used to represent integer numbers. e.g. -1, -2, -3
# float - used to represent real numbers. e.g. 1.2, 42.42
# boolean - used to represent True or False.
# complex - used to represent complex numbers. e.g. 1.0 + 2.0j, 1.5 + 2.5j

'''

'''
---------------------------------- Data Types in NumPy -----------------------------------
NumPy has some extra data types, and refer to data types with one character, like i for integers, u for unsigned integers etc.

Below is a list of all data types in NumPy and the characters used to represent them.

i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )

'''

# Checking the Data Type of an Array
# The NumPy array object has a property called {dtype} that returns the data type of the array:
# Syntax: dtype


import numpy as np
arr = np.array([1, 2, 3, 4])

print(arr.dtype)

# arr = np.array(['apple1apple1', 'apple1banana1', 'cherry'])

# print(arr.dtype)


# # Creating Arrays With a Defined Data Type
# '''
# We use the array() function to create arrays,
# this function can take an optional argument: dtype that allows us to define the expected data type of the array elements:
# '''
# arr = np.array([1, 2, 3, 4], dtype='S')

# print(arr)
# print(arr.dtype)

arr = np.array([1, 2, 3, 4], dtype='S')

print(arr)
print(arr.dtype)
