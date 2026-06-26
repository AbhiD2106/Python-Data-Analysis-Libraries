import seaborn as sns
import matplotlib.pyplot as plt 
import numpy as np


#show all dataset
s = sns.get_dataset_names()
print(s)

a = sns.load_dataset('penguins')
ab = a.head()
print("\n" , ab)
print("\n" , a['species'].value_counts())
print("\n" , a['island'].value_counts())


sns.scatterplot(data = a ,x = "flipper_length_mm" , y = "body_mass_g" , hue = "island")
plt.legend()
plt.show()