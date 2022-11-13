import numpy as np 
import math 

#Array creation
a = np.array([1, 2, 3])
print(a)

# we can use ndim attribute to print the array. 
# this can tell us the demensions of the array
print(a.ndim)

#creating a matrix 
b = np.array([[1,2,3],[4,5,6]])
print(b)

#if we want to know the dimension of the array we use shape
print(b.shape)

#we can also check the type of items in the Array
print(a.dtype)

#we can also use float numbers in arrays
c = np.array([2.5,5.7,9.6])
print(c)
print(c.dtype.name)

d = np.array([[2.2,3.5,5.6],[4.6,7.8,9.8]])
print(d)
print(d.shape) 