# ======================================================
# Essential Pandas Methods: sort_values & drop_duplicates
# ======================================================

import pandas as pd
data = pd.read_csv('IPL.csv')

# ------------------------------------------------------
# sort_values Method
# ------------------------------------------------------

# The sort_values() method is commonly used in pandas.
# It's important to understand how to use it effectively.
# This method can be used on both Series and DataFrames.

# Example: Apply sort on a Series
team1_counts = data['team1'].value_counts()
team2_counts = data['team2'].value_counts()

# Combine both and sort the top 5 in descending order
total_matches = (team1_counts + team2_counts).head(5).sort_values(ascending=False)
print(total_matches)

# Example: Apply sort on a DataFrame
# Default is ascending order
data.sort_values('city')

# Descending order (non-permanent)
data.sort_values('city', ascending=False)

# To make the change permanent, use inplace=True
data.sort_values('city', ascending=False, inplace=True)

# ------------------------------------------------------
# Sorting with Multiple Columns
# ------------------------------------------------------

# Sort by city and then date (both ascending by default)
data.sort_values(['city', 'date']).head()

# Sort by city (ascending) and date (descending)
data.sort_values(['city', 'date'], ascending=[True, False]).head()

# ------------------------------------------------------
# drop_duplicates Method
# ------------------------------------------------------

# The drop_duplicates() method removes duplicate rows from the DataFrame.

# Example: Drop duplicate cities (IPL is held in 31 cities)
data.drop_duplicates(subset=['city'])
data.drop_duplicates(subset=['city']).shape

# Drop duplicates based on multiple columns
# Example: Get one match per city per season
data.drop_duplicates(subset=['city', 'season'])
data.drop_duplicates(subset=['city', 'season']).shape

# Example: Find the winner of each IPL season
data.drop_duplicates('season', keep='last')[['season', 'winner']].sort_values('season')