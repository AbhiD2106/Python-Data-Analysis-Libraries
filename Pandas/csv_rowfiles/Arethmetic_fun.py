import pandas as py
import numpy as np

df = py.read_csv(r'E:\my_work\Python_libs\Python-Data-Analysis-Libraries\Pandas\csv_rowfiles\kohli_ipl.csv')
print(df)

#count

print("\n vk runs: ",df.count())

#sum

sub = py.read_csv(r'E:\my_work\Python_libs\Python-Data-Analysis-Libraries\Pandas\csv_rowfiles\subs.csv')
print("\n",sub)

print("\n sum of sub :" , sub.sum())

#product

print("\n product (multiplication) of sub :" , sub.product())

#mean > median > mode > std > var

print("\n 1 year sub " , sub.mean())
print("\n median score of vk /" , df.median())

movie = py.read_csv(r'E:\my_work\Python_libs\Python-Data-Analysis-Libraries\Pandas\csv_rowfiles\bollywood.csv')
print("\n",movie)

#mode - gives that value which comes many time in table 

print("\n no of movie which comes many times : " , movie.mode())

#std 

print("\n std of sub " , sub.std())

#min \ max

print("\n min sub : " , sub.min())
print("\n max sub : " , sub.max())

#describe:
#write summary

print("\n describe of sub " , sub.describe())
print("\n describe score of vk /" , df.describe())


