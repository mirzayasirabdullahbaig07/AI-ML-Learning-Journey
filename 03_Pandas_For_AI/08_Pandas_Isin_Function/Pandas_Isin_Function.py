import numpy as np
import pandas as pd

# Load the delivery dataset
delivery = pd.read_csv('deliveries.csv')

# Filter deliveries in the death overs (overs 16 to 20)
death_over = delivery[delivery['over'] > 15]

# Count the number of balls played by each batsman in death overs
balls_faced = death_over.groupby('batsman')['batsman_runs'].count()

# Filter batsmen who have faced more than 200 balls in death overs
eligible_batsmen = balls_faced[balls_faced > 200].index.tolist()

# Filter the original dataframe for only those batsmen
final = death_over[death_over['batsman'].isin(eligible_batsmen)]

# Calculate total runs scored in death overs by each eligible batsman
runs = final.groupby('batsman')['batsman_runs'].sum()

# Recalculate balls played (can also use count as earlier)
balls = final.groupby('batsman')['batsman_runs'].count()

# Calculate strike rate
strike_rate = (runs / balls) * 100

# Sort by strike rate in descending order to find the most destructive batsman
most_destructive = strike_rate.sort_values(ascending=False)

# Display the most destructive batsman(s) in death overs
print("Most Destructive Batsmen in IPL Death Overs (min 200 balls faced):\n")
print(most_destructive)

# Optional: display top 1
print("\nTop Most Destructive Batsman:")
print(most_destructive.head(1))
