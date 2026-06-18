import numpy as np  

#array operations
#scaler operations
#vector operations

a1 = np.arange(12).reshape(3, 4)
print("\n" , a1)

a2 = np.arange(12,24).reshape(3, 4) 
print("\n" , a2)

#scaler operations
#it means we are performing operations on each element of the array with a scaler value.

print("\n scaler multiplication")
print("\n" , a1 * 2)
print("\n" , a1 + 2)
print("\n" , a1 / 2)
print("\n" , a1 - 2)

#relational operations

print("\n relational operations : ")
print("\n" , a1 > 5)
print("\n" , a1 < 5)
print("\n" , a1 == 5)

#vector operations
#it means we are performing operations on two arrays of the same shape, element-wise.

print("\n vector addition")
print("\n" , a1 + a2)
print("\n vector subtraction")
print("\n" , a1 - a2)
print("\n vector multiplication")
print("\n" , a1 * a2)
print("\n vector division")
print("\n" , a1 / a2)
print("\n vector modulus")
print("\n" , a1 % a2)
print("\n vector floor division")
print("\n" , a1 // a2)