import numpy as np
import matplotlib.pyplot as plt


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