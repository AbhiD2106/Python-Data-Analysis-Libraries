import numpy as np
import matplotlib.pyplot as plt

# Data
x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 4, 9, 16, 25])

# Create a 2x2 subplot
figure, axes = plt.subplots(2, 2, figsize=(9,7))

# Top-left: Line Plot
axes[0, 0].plot(x, y, marker='o', color='blue')
axes[0, 0].set_title("Line Plot")
axes[0, 0].set_xlabel("X Values")
axes[0, 0].set_ylabel("Y Values")
axes[0, 0].grid(True)

# Top-right: Scatter Plot
axes[0, 1].scatter(x, y, color='red', s=80)
axes[0, 1].set_title("Scatter Plot")
axes[0, 1].set_xlabel("X Values")
axes[0, 1].set_ylabel("Y Values")
axes[0, 1].grid(True)

# Bottom-left: Bar Chart
axes[1, 0].bar(x, y, color='green')
axes[1, 0].set_title("Bar Chart")
axes[1, 0].set_xlabel("X Values")
axes[1, 0].set_ylabel("Y Values")
axes[1, 0].grid(axis='y')

# Bottom-right: Histogram
axes[1, 1].hist(y, bins=5, color='orange', edgecolor='black')
axes[1, 1].set_title("Histogram")
axes[1, 1].set_xlabel("Marks")
axes[1, 1].set_ylabel("Frequency")
axes[1, 1].grid(axis='y')

# Main title
figure.suptitle("Matplotlib Subplots Example", fontsize=16, fontweight='bold')

# Adjust spacing
plt.tight_layout()

# Display the figure
plt.show()  