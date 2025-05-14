# Pivot table function in pandas is used to summarize and aggregate data.
# It allows grouping by one or more columns and applying an aggregation function like mean, sum, or count.

import numpy as np
import pandas as pd

match = pd.read_csv("matches.csv")
delivery = pd.read_csv("deliveries.csv")

mask = delivery['batsman_runs']==6
six = delivery[mask]
six.shape

pt = six.pivot_table(index = 'over', columns = 'batting_team', values= 'batsman_runs', aggfunc = 'count')

# heatmap
import seaborn as sns
sns.heatmap(pt)
