#import numpy
import numpy as np

print("1D array")
a = np.array([1, 2, 3])
print(a)

#2d - 3D array
print("\n 2D array")
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)

print("\n 3D array")
c = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(c)


#dtype

a1 = np.array([1, 2, 3], dtype=float)
print("\n" ,  a1)

#arrange
print("\n arange")
d = np.arange(1, 11 )
print("\n", d)

print("\n alternate arange")
e = np.arange(1, 11, 2)
print("\n", e)

#reshape

print("\n reshape")
b1 = np.arange(1, 11 ).reshape(2, 5)
print("\n", b1)

#np.ones and no.zeros
#use is to create an array of given shape and type, filled with ones or zeros.

np1 = np.ones((2, 3))
print("\n np.ones")
print(np1)

np0 = np.zeros((2, 3))
print("\n np.zeros")
print(np0)


#no.random

np3 = np.random.rand(2, 5)
print("\n np.random.rand")
print(np3)

#np.linspace
#creates points equally spaced between a specified range. 
# It takes three parameters: start, stop, and num (number of points to generate).

np4 = np.linspace(-1, 10 , 10)
print("\n np.linspace") 
print(np4)

#shape

np5 = np.array([[1, 2, 3], [4, 5, 6]])
print("\n shape of np5")
print(np5.shape)

#size

print("\n size of np5")
print(np5.size)

#itemsize
#use is to get the size in bytes of each element in the array.

print("\n itemsize of np5")
print(np5.itemsize)

