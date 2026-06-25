import numpy as np
import matplotlib.pyplot as plt

# x = np.random.randint(1,150,10)
# print(x)
'''
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


'''

'''
#grid()

x = [1,2,3,4,5]
y = [5,10,15,20,25]

plt.grid(axis = "y",
         linewidth = 2 ,
         color = "lightgray",
         linestyle = "solid")

plt . plot(x,y)
plt.show()

'''

#barchart
'''
 
cat = np.array(["Grains", "Fruits", "Veggies", "Protein", "Dairy", "Sweets"])
values = np.array([5, 2, 1, 6, 2, 7])

plt.figure(figsize=(8,5))

plt.bar(
    cat,
    values,
    color="skyblue",
    edgecolor="black",
    width=0.5
)

plt.title("Food Categories")
plt.xlabel("Categories")
plt.ylabel("Values")

plt.grid(axis="y", linestyle="--")

plt.show()
 
 '''

#pie chart

cat = np.array(["Grains", "Fruits", "Veggies", "Protein", "Dairy", "Sweets"])
values = np.array([5, 2, 1, 6, 2, 7])
colors = ["gold", "orange", "limegreen", "deepskyblue", "violet", "tomato"]

plt.figure(figsize=(10,10))

plt.pie(
    values,
    labels=cat,
    colors=colors,
    autopct="%1.1f%%",
    startangle=90,
    explode=(0, 0, 0, 0.1, 0, 0)
)

plt.title("Food Categories", fontsize=15)
plt.axis("equal")   # Makes the pie chart a perfect circle
plt.legend()
plt.show()