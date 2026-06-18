import numpy as np

#concatenate

a1 = np.array([[1, 2], [3, 4]])
a2 = np.array([[5, 6], [7, 8]])

print("\n a1")
print(a1)
print("\n a2")
print(a2)

print("\n concatenate a1 and a2 along axis 0 (rows)")
print(np.concatenate((a1, a2), axis=0))
print("\n concatenate a1 and a2 along axis 1 (columns)")
print(np.concatenate((a1, a2), axis=1))


#unique

a = np.array([1 ,2, 2, 3, 4, 5, 5, 6,3, 7, 8, 8])
print("\n a")
print(a)
print("\n unique elements in a")
print(np.unique(a))

#where

np1 = np.random.randint(1, 100 , 15)
print("\n np1")
print(np1)

print("\n sorted np1")
print(np.sort(np1))

print("\n indices of np1 where elements are greater than 50")
print(np.where(np1 > 50))

print("\n indices of np1 where elements are less than 40")
print(np.where(np1 < 40))


#replace all vals >  50 replace with 0

print("\n np1 with values > 50 replaced with 0")
print(np.where(np1 > 50, 0, np1))

#replace even with  0

print("\n np1 with even values replaced with 0")
print(np.where(np1 % 2 == 0, 0, np1))

#isin 
#use for checking if elements of an array are present in another array.

a = np.array([1, 2, 3, 4, 5])
b = np.array([3, 4, 5, 6, 7])
print("\n a")
print(a)
print("\n b")
print(b)
print("\n check if elements of a are in b")
print(np.isin(a, b))


#flip

a = np.array([[1, 2], [3, 4]])
print("\n a")
print(a)
print("\n flip a vertically")
print(np.flip(a, axis=0))
print("\n flip a horizontally")
print(np.flip(a, axis=1))


#put
#use for editing elements of an array at specified indices.

a = np.array([1, 2, 3, 4, 5])
print("\n a")
print(a)
print("\n put 10 at index 2 and 20 at index 4")
np.put(a, [2, 4], [10, 20])
print("\n a after put")
print(a)


#delete

a = np.array([1, 2, 3, 4, 5])
print("\n a")
print(a)
print("\n delete element at index 2")
a = np.delete(a, 2)
print("\n a after delete")
print(a)


#set functions
#this is all set fun
#use for finding unique elements, union, intersection, and difference of arrays.

m = np.array([1, 2, 3, 4, 5])
n = np.array([4, 5, 6, 7, 8])
print("\n m")
print(m)
print("\n n")
print(n)

print("\n unique elements in m")
print(np.unique(m))
print("union of m and n")
print(np.union1d(m, n))
print("\n intersection of m and n")
print(np.intersect1d(m, n))
print("\n difference of m and n")
print(np.setdiff1d(m, n))
