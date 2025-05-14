# In this repository, we are going to learn two important functions in Pandas:
# 1. The `corr()` function — for correlation analysis
# 2. The `rename()` function — for renaming columns

# --------------------------------------
# What is the `corr()` function in Pandas?
# The correlation function is used to check the statistical relationship (correlation) between two numerical columns.
# It tells us how two variables vary with respect to each other.
# Sometimes we observe that increasing one variable may increase or decrease another — this is known as correlation.
# 
# - A correlation value of **1** means a perfect positive relationship (both increase together).
# - A value of **-1** indicates a perfect negative relationship (one increases, the other decreases).
# - A value of **0** means no relationship at all.

# View correlation matrix

import numpy as np
import pandas as pd

matches = pd.read_csv("matches.csv")
matches.corr()

# Visualize correlation matrix using a heatmap
import seaborn as sns
sns.heatmap(matches.corr(), annot=True, cmap='coolwarm')

# --------------------------------------
# Rename Columns using `rename()` function

# Syntax: DataFrame.rename(columns={'old_name': 'new_name'})
# This is a temporary change (returns a new DataFrame unless `inplace=True` is used)

matches.rename(columns={'city': 'place', 'date': 'all_dates'})  # Temporary renaming

# If you want to rename permanently, use `inplace=True`
# Example:
# matches.rename(columns={'city': 'place', 'date': 'all_dates'}, inplace=True)
