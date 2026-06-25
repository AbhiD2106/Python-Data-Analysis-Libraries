import numpy as np
import matplotlib.pyplot as plt

# Generate random scores
scores = np.random.normal(loc=20, scale=10, size=100)

# Create figure
plt.figure(figsize=(7, 5))

# Histogram
plt.hist(scores, bins=15, color="skyblue", edgecolor="black")

# Title and labels
plt.title("Distribution of Scores", fontsize=16, fontweight="bold")
plt.xlabel("Scores", fontsize=12)
plt.ylabel("Frequency", fontsize=12)

# Grid
plt.grid(axis="y", linestyle="--", alpha=0.5)

# Show plot
plt.show()