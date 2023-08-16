'''
# Create a NumPy ndarray Object
NumPy is used to work with arrays. The array object in NumPy is called ndarray.

We can create a NumPy ndarray object by using the array() function.
'''


import numpy as np

#  Difference between list and numpy_Array:-

# list Example
list_arr = [1, 2, 3]
# print(list_arr)
# print(type(list_arr))


# Numpy Array Example
arr = np.array([1, 2, 3])
# print(arr)
# print(type(arr))

'''
# Dimensions in Arrays
A dimension in arrays is one level of array depth (nested arrays).

nested array: are arrays that have arrays as their elements.
'''
# 0-D Arrays
# 0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.

# Example of 0-D Arrays:-

arr = np.array(24)
# print(arr)  # 24

# 1-D Arrays
# An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.
# These are the most common and basic arrays.

# Example of 1-D Arrays:-

arr = np.array([24, 2, 3])
# print(arr) # [24  2  3]

# 2-D Arrays
# An array that has 1-D arrays as its elements is called a 2-D array.
# These are often used to represent matrix or 2nd order tensors.
# NumPy has a whole sub module dedicated towards matrix operations called numpy.mat

arr = np.array([[24, 1, 2], [25, 26, 27]])
# print(arr)
'''
[[24  1  2]
 [25 26 27]]
 '''

# 3-D arrays
# An array that has 2-D arrays (matrices) as its elements is called 3-D array.
# These are often used to represent a 3rd order tensor.

# Example of 3-D Arrays:-
# Create a 3-D array with two 2-D arrays, both containing two arrays with the values 1,2,3 and 4,5,6:


arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
# print(arr)
''' [[[1 2 3]
  [4 5 6]]

 [[1 2 3]
  [4 5 6]]]
'''
# Check Number of Dimensions?
# NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.

# Example of Number of Dimensions
# Check how many dimensions the arrays have:

'''
syntax: ndim 
used to count number of dimensions.
'''

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

# print(a.ndim)  # 0
# print(b.ndim)  # 1
# print(c.ndim)  # 2
# print(d.ndim)  # 3


'''
type(): This built-in Python function tells us the type of the object passed to it. Like in above code it shows that arr is numpy.ndarray type.

To create an ndarray, we can pass a list, tuple or any array-like object into the array() method, and it will be converted into an ndarray:

Example
Use a tuple to create a NumPy array:

import numpy as np

arr = np.array((1, 2, 3, 4, 5))

print(arr)
'''

# Higher Dimensional Arrays
# An array can have any number of dimensions.
# When the array is created, you can define the number of dimensions by using the ndmin argument.

# Syntax: ndmin
'''
arr = np.array([1, 2, 3, 4], ndmin=6)

print(arr) #[[[[[[1 2 3 4]]]]]]
print('number of dimensions :', arr.ndim) #number of dimensions : 6

-----> In this array the innermost dimension (5th dim) has 4 elements, the 4th dim has 1 element that is the vector, the 3rd dim has 1 element that is the matrix with the vector, the 2nd dim has 1 element that is 3D array and 1st dim has 1 element that is a 4D array.
'''
