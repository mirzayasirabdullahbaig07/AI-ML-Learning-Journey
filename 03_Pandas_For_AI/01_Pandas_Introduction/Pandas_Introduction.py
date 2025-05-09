# What is the Pandas library?
# Pandas is a powerful open-source data analysis and manipulation tool built on top of the Python programming language.

# Why do we use Pandas?
# Pandas makes it easy to clean, analyze, explore, and visualize structured data efficiently.

# What is the functionality of the Pandas library?
# Pandas provides two main data structures:
# 1. DataFrame: A 2-dimensional labeled data structure (like an Excel table or SQL table).
# 2. Series: A 1-dimensional labeled array (like a single row or column from a DataFrame).

# In this example, we'll work with an IPL dataset.

# Step 1: Download the dataset in CSV format
# Link: https://docs.google.com/spreadsheets/d/1lhoRGl8lm-_Rx2H1kman6wSZS0Bfa0BhtV1vouKyaCM/edit?gid=870045902
# Go to File > Download > Comma-separated values (.csv)

# Step 2: Upload the CSV file to your working environment (Google Colab, Jupyter Notebook, or VS Code)

# Step 3: Import required libraries
import numpy as np
import pandas as pd

# Step 4: Load the dataset using Pandas
data = pd.read_csv('IPL.csv')  # Replace 'IPL.csv' with your actual file name if different

# Step 5: Verify the type of the loaded data
print("Type of data object:", type(data))  # Should return <class 'pandas.core.frame.DataFrame'>