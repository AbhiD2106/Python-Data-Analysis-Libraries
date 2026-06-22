import numpy as  np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#2d line ploat
#use biveriate analysis
#apply on 2 column
#numerical another categorical or numerical to numerical
#use case : time series data

#ploating a simple fun

price = [40000,23333,59994,82888,86838,47222,75633]
year = [2022,2023,2024,2025,2026,2027,2028]

#(X axis , Y axis)
# plt.plot(year,price)
# plt.show()

#use with data set

batter = pd.read_csv(r'E:\my_work\Python_libs\Python-Data-Analysis-Libraries\Matplotlib\dataset\sharma-kohli.csv')
print("\n" , batter)


# plt.plot(batter['index'],batter['V Kohli'])
# plt.plot(batter['index'],batter['RG Sharma'])
# plt.title('rohit VS kohli')
# plt.xlabel('season of ipl')
# plt.ylabel('run scored')
# plt.show() 


#styles

#linestyles -   dashed , dotted , solid , dashdot
#marker - d , + , > , < , O 

# plt.plot(batter['index'],batter['V Kohli'],color='#D10011',linestyle='dashdot',linewidth=3)
# plt.plot(batter['index'],batter['RG Sharma'],color='#008CFF',linestyle='dashdot',linewidth=2,marker='d' , markersize = 5)

# plt.title('rohit VS kohli')
# plt.xlabel('season of ipl')
# plt.ylabel('run scored')

# plt.show() 


#Allocation  line 

plt.plot(batter['index'],batter['V Kohli'],color='#D10011',linestyle='dashdot',linewidth=3 , label = 'virat')
plt.plot(batter['index'],batter['RG Sharma'],color='#008CFF',linestyle='dashdot',linewidth=2,marker='d' , markersize = 5 , label = 'rohit')

plt.title('rohit VS kohli')
plt.xlabel('season of ipl')
plt.ylabel('run scored')
plt.legend()        

plt.show() 