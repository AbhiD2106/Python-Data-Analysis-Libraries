import numpy as np
import pandas as pd

# Create a Series from a list

data = [10, 20, 30, 40, 50]
print(pd.Series(data))

countries = ['USA', 'Canada', 'Germany', 'UK', 'France']
print("\n",pd.Series(countries))

#custom index

marks = [85, 90, 78, 92, 88]
subjects = ['Math', 'Science', 'English', 'History', 'Art']
print("\n", pd.Series(marks, index=subjects))

#setting a name for the Series
marks = pd.Series(marks, index=subjects , name='Abhi Marks')
print("\n", marks)

# Create a Series with a dictionary

marks = {

    'Math': 85,
    'Science': 90,
    'English': 78,
    'History': 92,
    'Art': 88

}

marks_series = pd.Series(marks, name='Abhi Marks')
print("\n", marks_series)


#series  attributes

#size

print("\nSize of the Series:", marks_series.size)

#dtype

print("\nData type of the Series:", marks_series.dtype)

#name

print("\nName of the Series:", marks_series.name)

#is_unique
#it  says whether the values in the Series are unique or not

print("\nAre the values in the Series unique? =", marks_series.is_unique)
l1 = [1, 2, 3,4,2,1,53,32,11,33,33 ,4, 5]
print("\nAre the values in the Series unique? =", pd.Series(l1).is_unique)

#index

print("\nIndex of the Series:", marks_series.index)

#values

print("\nValues of the Series:", marks_series.values)