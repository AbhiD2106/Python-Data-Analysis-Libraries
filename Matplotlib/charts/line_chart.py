import numpy as np
import matplotlib.pyplot as plt

# x = np.random.randint(1,150,10)
# print(x)

x = np.array([2023,2024,2025,2026])
y = np.array([43,23,53,12])
y1 = np.array([21,32,92,45])
y2 = np.array([35,23,24,20])


line_style = dict(marker = "."
                ,markersize = 12
                ,markerfacecolor = "cyan"
                ,markeredgecolor = "#1cd3fc"
                ,linestyle = "dashdot",
                linewidth = 2,
                )

title_dic = dict( 
                 family = "Arial",
                 fontweight = "bold",
                 color = "black")


plt.xlabel("year",**title_dic,fontsize = 10)

plt.title("class size " , **title_dic ,fontsize = 20)
plt.plot(x,y,**line_style,color = "red")
plt.plot(x,y1,**line_style , color = "blue")
plt.plot(x,y2,**line_style , color = "yellow")
plt.xticks(x)
plt.show()


#grid()

x = [1,2,3,4,5]
y = [5,10,15,20,25]

plt.grid(axis = "y",
         linewidth = 2 ,
         color = "lightgray",
         linestyle = "solid")

plt . plot(x,y)
plt.show()



