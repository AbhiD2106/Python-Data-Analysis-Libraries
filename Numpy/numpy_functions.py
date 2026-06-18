import numpy as np

#functions

a1 = np.random.rand(3,3)
a1 = np.round(a1*100)
print("\n " , a1)

#max / min / sum / prod = multiplication / mean

print("\n max")
print(np.max(a1))
print("\n min")
print(np.min(a1))
print("\n sum")
print(np.sum(a1))
print("\n prod")
print(np.prod(a1))
print("\n mean")
print(np.mean(a1))

#every row min val

print("\n ", a1)

print("\n every row min val")
print(np.min(a1, axis=1))
print("\n every column min val")
print(np.min(a1, axis=0))

print("\n every row max val")
print(np.max(a1, axis=1))
print("\n every column max val")
print(np.max(a1, axis=0))

print("\n every row sum")
print(np.sum(a1, axis=1))
print("\n every column sum")
print(np.sum(a1, axis=0))   

print("\n every row prod")
print(np.prod(a1, axis=1))
print("\n every column prod")
print(np.prod(a1, axis=0))

#statistics functions

print("\n mean")
print(np.mean(a1))
print("\n median")
print(np.median(a1))
print("\n standard deviation")
print(np.std(a1))
print("\n variance")
print(np.var(a1))

#-----------------------------------------------------------------------------------------------
#sort

print("\n sort")
q = np.random.randint(1,100,15)
print(q)

print("\n sorted q")
print(np.sort(q))

b = np.random.randint(1,100,(6,4))
print("\n" , b)

print("\n sorted b : ")
print(np.sort(b , axis=0)) #sort each column
print("\n sorted b : ")
print(np.sort(b , axis=1)) #sort each row

#desc

print("\n sorted b in descending order : ")
print(np.sort(b , axis=0)[::-1]) #sort each column in descending order

#np.append

a = np.array([1, 2, 3])
print("\n a")
print(a)
print("\n append 4 to a")
a = np.append(a, 4)
print("\n a after append")
print(a)

#in 2d column append

b = np.array([[1, 2, 3], [4, 5, 6]])
print("\n b")       
print(b)
print("\n append a column of 7,8 to b")
b = np.append(b, [[7], [8]], axis=1)
print("\n b after append")
print(b)