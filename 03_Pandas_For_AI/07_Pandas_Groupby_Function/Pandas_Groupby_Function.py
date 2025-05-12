# GroupBy Analysis in Pandas and IPL Dataset

import numpy as np
import pandas as pd

# Load the Fortune 500 dataset
company = pd.read_csv('fortune500.csv', encoding='ISO-8859-1').head()

# Group by 'Sector'
sectors = company.groupby('Sector')

# Basic Analysis
print("Total companies:", len(company))  # Should be 500 for full data
print("Total sectors:", len(sectors))    # Number of unique sectors

# Size of each group
print(sectors.size().sort_values(ascending=False))

# First and last company in each sector
print(sectors.first())
print(sectors.last())

# Groups dictionary: sector -> list of indices
print(sectors.groups)

# Get specific group
print(sectors.get_group('Energy'))
print(sectors.get_group('Apparel').shape)

# Aggregate calculations
print(sectors.sum(numeric_only=True))
print(sectors.mean(numeric_only=True))

# Mean Revenues by Sector
print(sectors['Revenues'].mean().sort_values(ascending=False))

# -------------------- IPL Dataset Analysis --------------------

# Load IPL deliveries dataset
delivery = pd.read_csv('deliveries.csv')

# Group by batsman
runs = delivery.groupby('batsman')

# Balls played by Virat Kohli
print("Balls played by V Kohli:", runs.get_group('V Kohli').shape[0])

# Top 10 run scorers
print(runs['batsman_runs'].sum().sort_values(ascending=False).head(10))

# Batsman who hit the most fours
fours = delivery[delivery['batsman_runs'] == 4]
print("Total fours:", fours.shape[0])
print(fours.groupby('batsman')['batsman_runs'].count().sort_values(ascending=False).head(10))

# Virat Kohli's performance against bowling teams
vk = delivery[delivery['batsman'] == 'V Kohli']
print(vk.groupby('bowling_team')['batsman_runs'].sum().sort_values(ascending=False).head(3))

# General function to get top 3 scores against teams for any batsman
def run_scored(batsman_name):
    player_data = delivery[delivery['batsman'] == batsman_name]
    return player_data.groupby('bowling_team')['batsman_runs'].sum().sort_values(ascending=False).head(3)

print(run_scored('V Kohli'))
