import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

patient = pd.read_csv(r'E:\my_work\Python_libs\Python-Data-Analysis-Libraries\Data_Clean\patients.csv')
treatments = pd.read_csv(r'E:\my_work\Python_libs\Python-Data-Analysis-Libraries\Data_Clean\treatments.csv')
adverse_reactions = pd.read_csv(r'E:\my_work\Python_libs\Python-Data-Analysis-Libraries\Data_Clean\adverse_reactions.csv')


# Patients Dataset Cleaning

# Remove duplicate rows
patient.drop_duplicates(inplace=True)

# Remove duplicate patient IDs (keep first)
patient.drop_duplicates(subset='patient_id', keep='first', inplace=True)

# Standardize text columns
text_cols = patient.select_dtypes(include='object').columns
for col in text_cols:
    patient[col] = patient[col].str.strip()

# Convert birthdate to datetime
if 'birthdate' in patient.columns:
    patient['birthdate'] = pd.to_datetime(patient['birthdate'], errors='coerce')

# Fill missing address
if 'address' in patient.columns:
    patient['address'].fillna('Unknown', inplace=True)

# Fill missing gender with mode
if 'gender' in patient.columns:
    patient['gender'].fillna(patient['gender'].mode()[0], inplace=True)

# Remove impossible values
if 'height' in patient.columns:
    patient.loc[(patient['height'] < 50) | (patient['height'] > 250), 'height'] = np.nan

if 'weight' in patient.columns:
    patient.loc[(patient['weight'] < 20) | (patient['weight'] > 300), 'weight'] = np.nan

# Fill missing height and weight
if 'height' in patient.columns:
    patient['height'].fillna(patient['height'].median(), inplace=True)

if 'weight' in patient.columns:
    patient['weight'].fillna(patient['weight'].median(), inplace=True)


# Treatments Dataset Cleaning

# Remove duplicate rows
treatments.drop_duplicates(inplace=True)

# Replace '-' with NaN
treatments.replace('-', np.nan, inplace=True)

# Convert numeric columns
numeric_cols = [
    'hba1c_start',
    'hba1c_end',
    'hba1c_change'
]

for col in numeric_cols:
    if col in treatments.columns:
        treatments[col] = pd.to_numeric(treatments[col], errors='coerce')

# Calculate missing HbA1c change
if all(col in treatments.columns for col in ['hba1c_start', 'hba1c_end', 'hba1c_change']):
    mask = treatments['hba1c_change'].isna()
    treatments.loc[mask, 'hba1c_change'] = (
        treatments.loc[mask, 'hba1c_end'] -
        treatments.loc[mask, 'hba1c_start']
    )

# Adverse Reactions Dataset


# Remove duplicate rows
adverse_reactions.drop_duplicates(inplace=True)

# Standardize text
text_cols = adverse_reactions.select_dtypes(include='object').columns
for col in text_cols:
    adverse_reactions[col] = adverse_reactions[col].str.strip()

# ===========================
# Check Missing Values
# ===========================

print("\nPatients Missing Values")
print(patient.isnull().sum())

print("\nTreatments Missing Values")
print(treatments.isnull().sum())

print("\nAdverse Reactions Missing Values")
print(adverse_reactions.isnull().sum())

# ===========================
# Dataset Information
# ===========================

print("\nPatients Info")
print(patient.info())

print("\nTreatments Info")
print(treatments.info())

print("\nAdverse Reactions Info")
print(adverse_reactions.info())

# ===========================
# Save Cleaned Data
# ===========================

patient.to_csv("patients_clean.csv", index=False)
treatments.to_csv("treatments_clean.csv", index=False)
adverse_reactions.to_csv("adverse_reactions_clean.csv", index=False)

print("\nData cleaning completed successfully!")