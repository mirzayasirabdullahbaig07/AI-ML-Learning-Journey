# ===============================================
# Fetching Columns and Rows from a DataFrame
# ===============================================

# When working with datasets, it's common to fetch only the relevant columns or rows.
# This helps in focusing on important data and improving performance.

# ------------------------------------------------
# Fetching a Single Column
# ------------------------------------------------

# import numpy as np
import pandas as pd

data = pd.read_csv('IPL.csv')

# Let's say we want to extract the 'winner' column from the DataFrame named 'data'.

data['winner']  # This returns a Series
type(data['winner'])  # Check the type: pandas Series has index and values
data['winner'].shape  # Returns the shape of the Series (number of rows,)

# ------------------------------------------------
# Fetching Multiple Columns
# ------------------------------------------------

# To fetch multiple columns, wrap column names inside a list:

data[['team1', 'team2', 'winner']]  # This returns a DataFrame
data[['team1', 'team2', 'winner']].shape  # Get the shape of the resulting DataFrame

# ------------------------------------------------
# Fetching Rows Using iloc
# ------------------------------------------------

# iloc is used for positional indexing (integer-location based)

data.iloc[0]        # Fetch the first row (index 0)
data.iloc[1]        # Fetch the second row (index 1)
data.iloc[1:3]      # Fetch rows at index 1 and 2 (Python slicing is exclusive of end)
data.iloc[1:11:2]   # Fetch every second row from index 1 to 10 (step = 2)
data.iloc[[1, 5, 6]]  # Fancy indexing: fetch rows 1, 5, and 6

# ------------------------------------------------
# Fetch Specific Columns for All Rows
# ------------------------------------------------

# Use iloc to fetch specific columns for all rows:

data.iloc[:, [4, 5, 10]]  # ':' means all rows, and [4, 5, 10] are the column positions

# Example: 4 = 'team1', 5 = 'team2', 10 = 'winner'

# iloc supports fancy indexing for both rows and columns.

