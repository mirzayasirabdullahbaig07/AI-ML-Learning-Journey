# ======================================================
# Visualizing Data with Charts in Pandas & Matplotlib
# ======================================================
import pandas as pd
data = pd.read_csv('IPL.csv')
import matplotlib.pyplot as plt

# ------------------------------------------------------
# Bar Chart
# ------------------------------------------------------

# A bar chart is used to represent categorical data with rectangular bars.
# Useful for comparing quantities across categories.

# Example: Number of matches won by each team
data['winner'].value_counts().plot(kind='bar')

# Horizontal bar chart (barh)
data['winner'].value_counts().plot(kind='barh')

# Top 5 teams with most wins
data['winner'].value_counts().head(5).plot(kind='bar')

# ------------------------------------------------------
# Pie Chart
# ------------------------------------------------------

# A pie chart is used to show proportions of a whole.
# Example: Toss decision distribution

data['toss_decision'].value_counts().plot(kind='pie', autopct='%1.1f%%')

# ------------------------------------------------------
# Histogram
# ------------------------------------------------------

# A histogram shows the distribution of a numeric variable.
# Example: Distribution of win margins by runs

data['win_by_runs'].plot(kind='hist', bins=20)