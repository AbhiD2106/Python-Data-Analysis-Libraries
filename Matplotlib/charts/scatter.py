import numpy as np
import matplotlib.pyplot as plt


# Data
x = np.array([0, 1, 1, 2, 3, 4, 5, 6, 7, 7, 8])   # Hours studied
y = np.array([55, 60, 65, 62, 68, 70, 75, 78, 82, 85, 87])  # Marks

x1 = np.array([0,1,2,2,3,4,5,6,7,8,8])   # Hours studied
y1 = np.array([50,36,76,42,65,97,65,54,45,86,64])  # Marks

plt.figure(figsize=(7, 5))

plt.scatter(x, y, color="red", s=60 ,alpha= 0.5 , edgecolor="black" , label = "class 1")
plt.scatter(x1, y1, color="royalblue", s=60 ,alpha= 1 , edgecolor="black" , label = "class 2")


plt.title("Test Scores", fontsize=16, fontweight="bold")
plt.xlabel("Hours Studied", fontsize=12)
plt.ylabel("Marks", fontsize=12)
plt.grid()
plt.legend()
plt.show()