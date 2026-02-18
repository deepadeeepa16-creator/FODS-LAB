from collections import Counter

# Sample dataset
data = [12, 15, 12, 18, 21, 15, 15, 18, 21, 21, 21, 25]

# Count frequencies
freq_dist = Counter(data)

# Display results
print("Value\tFrequency")
for value, freq in freq_dist.items():
    print(f"{value}\t{freq}")
