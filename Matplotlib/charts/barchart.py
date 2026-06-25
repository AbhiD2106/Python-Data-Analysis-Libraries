import numpy as np
import matplotlib.pyplot as plt
 
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
 