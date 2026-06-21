import numpy as np
import pandas as pd


'''
#with one column

df = pd.read_csv(r'E:\my_work\Python_libs\Python-Data-Analysis-Libraries\Pandas\csv_rowfiles\subs.csv' )
print(df)

#with multiple columns
#index_col is used to set the index of the dataframe to a specific column

df = pd.read_csv(r'E:\my_work\Python_libs\Python-Data-Analysis-Libraries\Pandas\csv_rowfiles\kohli_ipl.csv',index_col='match_no')
print(df)


'''


df_bollywood = pd.read_csv(r'E:\my_work\Python_libs\Python-Data-Analysis-Libraries\Pandas\csv_rowfiles\bollywood.csv')
print(df_bollywood)

#head tail

#head for previewing the first 5 rows of the dataframe

subs_df = pd.read_csv(r'E:\my_work\Python_libs\Python-Data-Analysis-Libraries\Pandas\csv_rowfiles\subs.csv' )
print(subs_df)

h = subs_df.head(5)
print(h)

#tail for previewing the last 5 rows of the dataframe

t = subs_df.tail(5)
print("\n ",t)


#sample
#use for randomly selecting rows from the dataframe

s= df_bollywood.sample(3)
print("\n ",s)

#value_counts   
#use for counting the occurrences of unique values in a column
#count no of movies by actor

vc = df_bollywood.value_counts()
print("\n ",vc)


#sort_values
#use for sorting the dataframe based on a specific column


df_vk = pd.read_csv(r'E:\my_work\Python_libs\Python-Data-Analysis-Libraries\Pandas\csv_rowfiles\kohli_ipl.csv',index_col='match_no')
print(df_vk)

sort = df_vk.sort_values("runs" , ascending=False).head(3)
print("\n",sort)


sort = df_vk.sort_values("runs")
print("\n",sort)


#sort values
#original dataset change in asc order   

si = df_vk.sort_values("runs" , inplace=True)
print("\n",si)

#inplace = true 
#parmenent change in csv filess

#sort index
#use for index order

print("\n" , df_bollywood.sort_index(inplace=True))

