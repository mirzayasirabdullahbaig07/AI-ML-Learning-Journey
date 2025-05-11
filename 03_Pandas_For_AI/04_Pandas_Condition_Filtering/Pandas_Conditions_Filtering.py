# ============================================================
# Filtering DataFrames with Conditions (Masking in Pandas)
# ============================================================

# This is a very important concept when working with DataFrames.
# The technique is known as *masking* — using boolean conditions
# to filter data.

# ------------------------------------------------------------
# Basic Masking: Filtering Based on a Condition
# ------------------------------------------------------------

# import numpy as np
import pandas as pd

data = pd.read_csv('IPL.csv')

# Example: Find all matches played in the city 'Hyderabad'

data['city'] == 'Hyderabad'  # Returns a Series of True/False (Boolean Series)

# Note: If you see index on the left and values on the right, it's a Series.

mask = data['city'] == 'Hyderabad'
data[mask]  # Returns only the rows where the city is 'Hyderabad'

# Number of matches played in Hyderabad
data[mask].shape[0]

# ------------------------------------------------------------
# Creating a Reusable Function to Count Matches in a City
# ------------------------------------------------------------

def get_match_count(city):
    mask = data['city'] == city
    return data[mask].shape[0]

# Example usage:
print(get_match_count("Mumbai"))

# ------------------------------------------------------------
# Combining Multiple Conditions
# ------------------------------------------------------------

# Example: Find how many matches were played in Hyderabad *after 2010*

mask1 = data['city'] == 'Hyderabad'
mask2 = data['date'] > '2010-01-01'

# Use '&' to combine conditions (AND logic)
data[mask1 & mask2].shape[0]

# ------------------------------------------------------------
# Value Counts in a Series
# ------------------------------------------------------------

# The value_counts() function is used on Series (especially categorical data)
# to count the frequency of unique values.

# Example: Find out which team has won the most matches

data['winner'].value_counts()
