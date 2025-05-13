import pandas as pd

# Load the datasets
delivery = pd.read_csv('deliveries.csv')
matches = pd.read_csv('matches.csv')

# Merge the datasets using match ID (common key in both datasets)
# 'match_id' in deliveries corresponds to 'id' in matches
# merge() combines rows from both DataFrames where keys match
merged = delivery.merge(matches, left_on='match_id', right_on='id')

# Total runs scored by each batsman in each season
# groupby() groups the data by season and batsman
# sum() calculates total runs scored
season_runs = merged.groupby(['season', 'batsman'])['batsman_runs'].sum().reset_index()

# Sort by season and runs scored in descending order
# This helps in identifying the top scorer for each season
season_runs_sorted = season_runs.sort_values(['season', 'batsman_runs'], ascending=[True, False])

# Get the top run scorer (Orange Cap holder) for each season
# drop_duplicates() keeps only the first entry per season (which is the highest scorer due to sorting)
orange_cap_holders = season_runs_sorted.drop_duplicates(subset='season', keep='first')

# Display only the season and batsman name (Orange Cap holder)
# Also include the total runs scored for reference
orange_cap_holders = orange_cap_holders[['season', 'batsman', 'batsman_runs']].reset_index(drop=True)

# Output the result
print("Orange Cap Holders (Leading Run Scorers) by IPL Season:\n")
print(orange_cap_holders)
