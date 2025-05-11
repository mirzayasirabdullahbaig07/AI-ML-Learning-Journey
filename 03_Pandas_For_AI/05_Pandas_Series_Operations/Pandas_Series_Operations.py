# ======================================================
# What Are Series in Pandas
# ======================================================
import pandas as pd
data = pd.read_csv('IPL.csv')

# ------------------------------------------------------
# Series Basics
# ------------------------------------------------------

# Series are the building blocks in pandas.
# A Series is a one-dimensional labeled array.
# When you fetch a single row or a single column from a DataFrame, it returns a Series.
# Some pandas functions (like value_counts()) also return a Series.

# ------------------------------------------------------
# Series Terminology
# ------------------------------------------------------

# A Series has two parts:
# - Index (left side): must be unique.
# - Values (right side): can be repeated.

# Example: Get a Series of match wins
myseries = data['winner'].value_counts()

# Get only the index (team names)
myseries.index

# Get only the values (number of wins)
myseries.values

# View the top and bottom entries
myseries.head()
myseries.tail()

# ------------------------------------------------------
# Accessing Series Values
# ------------------------------------------------------

# You can get a single value from a Series using its index
myseries['Pune Warriors']

# ------------------------------------------------------
# Practical Example: Team with Most Matches Played
# ------------------------------------------------------

# Count appearances as team1 and team2
team1_counts = data['team1'].value_counts()
team2_counts = data['team2'].value_counts()

# Add both series to get total matches played by each team
total_matches = team1_counts + team2_counts
print(total_matches)

# ------------------------------------------------------
# Mathematical Operations on Series
# ------------------------------------------------------

# You can perform mathematical operations on Series if:
# - Their indexes match.
# - The operation has logical meaning.