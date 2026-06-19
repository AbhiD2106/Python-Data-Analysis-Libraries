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


# df_bollywood = pd.read_csv(r'E:\my_work\Python_libs\Python-Data-Analysis-Libraries\Pandas\csv_rowfiles\bollywood.csv')
# print(df_bollywood)

#head tail

#head for previewing the first 5 rows of the dataframe

subs_df = pd.read_csv(r'E:\my_work\Python_libs\Python-Data-Analysis-Libraries\Pandas\csv_rowfiles\subs.csv' )
print(subs_df)

h = subs_df.head(5)
print(h)