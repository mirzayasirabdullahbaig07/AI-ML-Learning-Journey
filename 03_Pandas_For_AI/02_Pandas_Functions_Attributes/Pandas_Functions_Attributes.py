# Importing necessary library
import pandas as pd

# Load your dataset
# Example: Replace with your actual dataset path
data = pd.read_csv('your_dataset.csv')

# -----------------------------------------------
# 1. Preview the dataset

# Display the first few rows of the dataset
print("First 5 rows of the dataset:")
print(data.head())          # First 5 rows by default

print("\nFirst 3 rows of the dataset:")
print(data.head(3))         # First 3 rows

# Display the last few rows of the dataset
print("\nLast 5 rows of the dataset:")
print(data.tail())          # Last 5 rows by default

print("\nLast 3 rows of the dataset:")
print(data.tail(3))         # Last 3 rows

# -----------------------------------------------
# 2. Dataset Dimensions

print("\nShape of the dataset:")
print(data.shape)           # Output: (rows, columns)

# -----------------------------------------------
# 3. Dataset Information

print("\nInfo about the dataset:")
data.info()                 # Displays column names, non-null counts, and data types

# -----------------------------------------------
# 4. Descriptive Statistics (Numerical Columns Only)

print("\nDescriptive statistics for numerical columns:")
print(data.describe())      # Count, mean, std, min, max, etc.
