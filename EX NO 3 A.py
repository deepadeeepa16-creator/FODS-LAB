import pandas as pd

# Sample dataset
data = [12, 15, 12, 18, 21, 15, 15, 18, 21, 21, 21, 25]

# Convert to pandas Series
series = pd.Series(data)

# Define bins (intervals)
bins = [10, 15, 20, 25, 30]

# Create frequency distribution table
freq_table = pd.cut(series, bins=bins).value_counts().sort_index()

print("Interval\tFrequency")
for interval, freq in freq_table.items():
    print(f"{interval}\t{freq}")
