import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
train = pd.read_csv(r'E:\my_work\Python_libs\Python-Data-Analysis-Libraries\EDA\train.csv')

# ----------------------------
# Basic Information
# ----------------------------

print("First 5 Rows")
print(train.head())

print("\nLast 5 Rows")
print(train.tail())

print("\nShape of Dataset")
print(train.shape)

print("\nColumn Names")
print(train.columns)

print("\nDataset Information")
print(train.info())

print("\nData Types")
print(train.dtypes)

print("\nStatistical Summary")
print(train.describe())

# ----------------------------
# Missing Values
# ----------------------------

print("\nMissing Values")
print(train.isnull().sum())

# ----------------------------
# Duplicate Rows
# ----------------------------

print("\nDuplicate Rows")
print(train.duplicated().sum())

# ----------------------------
# Unique Values
# ----------------------------

print("\nUnique Values in Sex")
print(train["Sex"].unique())

print("\nUnique Values in Embarked")
print(train["Embarked"].unique())

print("\nUnique Values in Passenger Class")
print(train["Pclass"].unique())

# ----------------------------
# Value Counts
# ----------------------------

print("\nGender Count")
print(train["Sex"].value_counts())

print("\nPassenger Class Count")
print(train["Pclass"].value_counts())

print("\nSurvival Count")
print(train["Survived"].value_counts())

print("\nEmbarked Count")
print(train["Embarked"].value_counts())

# ----------------------------
# Age Analysis
# ----------------------------

print("\nAge Statistics")
print(train["Age"].describe())

plt.figure(figsize=(8,5))

train["Age"].plot(
    kind="hist",
    bins=20,
    color="skyblue",
    edgecolor="black"
)

plt.title("Age Distribution", fontsize=15, fontweight="bold")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()

# ----------------------------
# Fare Analysis
# ----------------------------

print("\nFare Statistics")
print(train["Fare"].describe())

plt.figure(figsize=(8,5))

train["Fare"].plot(
    kind="hist",
    bins=20,
    color="orange",
    edgecolor="black"
)

plt.title("Fare Distribution", fontsize=15, fontweight="bold")
plt.xlabel("Fare")
plt.ylabel("Frequency")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()

# ----------------------------
# Passenger Class
# ----------------------------

plt.figure(figsize=(6,4))

train["Pclass"].value_counts().sort_index().plot(
    kind="bar",
    color=["#4E79A7","#F28E2B","#59A14F"],
    edgecolor="black"
)

plt.title("Passenger Class", fontsize=15, fontweight="bold")
plt.xlabel("Class")
plt.ylabel("Passengers")
plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()

# ----------------------------
# Gender Distribution
# ----------------------------

plt.figure(figsize=(6,4))

train["Sex"].value_counts().plot(
    kind="bar",
    color=["#5DADE2","#F1948A"],
    edgecolor="black"
)

plt.title("Gender Distribution", fontsize=15, fontweight="bold")
plt.xlabel("Gender")
plt.ylabel("Passengers")
plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()

# ----------------------------
# Survival Distribution
# ----------------------------

plt.figure(figsize=(6,4))

train["Survived"].value_counts().plot(
    kind="bar",
    color=["tomato","mediumseagreen"],
    edgecolor="black"
)

plt.title("Survival Count", fontsize=15, fontweight="bold")
plt.xlabel("0 = Not Survived    1 = Survived")
plt.ylabel("Passengers")
plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()

# ----------------------------
# Embarked Distribution
# ----------------------------

plt.figure(figsize=(6,4))

train["Embarked"].value_counts().plot(
    kind="bar",
    color=["#3498DB","#2ECC71","#F1C40F"],
    edgecolor="black"
)

plt.title("Embarked Port", fontsize=15, fontweight="bold")
plt.xlabel("Port")
plt.ylabel("Passengers")
plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()

# ----------------------------
# Age Boxplot
# ----------------------------

plt.figure(figsize=(8,2))

plt.boxplot(
    train["Age"].dropna(),
    vert=False,
    patch_artist=True
)

plt.title("Age Boxplot", fontsize=15, fontweight="bold")
plt.xlabel("Age")
plt.tight_layout()
plt.show()

# ----------------------------
# Fare Boxplot
# ----------------------------

plt.figure(figsize=(8,2))

plt.boxplot(
    train["Fare"],
    vert=False,
    patch_artist=True
)

plt.title("Fare Boxplot", fontsize=15, fontweight="bold")
plt.xlabel("Fare")
plt.tight_layout()
plt.show()