# In this section, we will learn some essential methods in Pandas:
# 1. set_index()
# 2. reset_index()
# 3. dropna()
# 4. fillna()

import numpy as np
import pandas as pd

# Load data
data = pd.read_csv('IPL.csv')
print(data)

# ----------------------------------------
# set_index()
# Used to set a specific column as the index of the DataFrame

data.set_index('id')  # Temporary change
data.set_index('id', inplace=True)  # Permanent change

# ----------------------------------------
# reset_index()
# Resets the index back to default integer index

data.reset_index()  # Temporary
data.reset_index(inplace=True)  # Permanent

# When applied to a Series, it converts it to a DataFrame
data['winner'].value_counts()  # Returns a Series

# Resetting index on the Series
data['winner'].value_counts().reset_index()

# ----------------------------------------
# Handling Missing Values

# dropna() → removes missing values

data.shape  # Check original shape

data.dropna()  # Drops rows with any missing value (temporary)

# Parameters:
# how = 'any' → drop row if any column has NaN
# how = 'all' → drop row only if all columns are NaN
# axis = 0 → drop rows
# axis = 1 → drop columns
# subset = list of columns to consider for NaN checks (acts like OR/union logic)

data.dropna(subset=['team'])
data.dropna(subset=['team', 'date'])  # Drops row if either column has NaN

# ----------------------------------------
# fillna() → fills missing values

data.fillna(0)  # Replaces all NaNs with 0 (good for numeric columns)

# For specific column (e.g., string values)
data['team'].fillna("not specified", inplace=True)

# Fill missing values using forward fill (ffill) or backward fill (bfill)
data['age'].fillna(method='bfill')  # Backward fill

# You can also use:
# data['age'].fillna(method='ffill')  # Forward fill
