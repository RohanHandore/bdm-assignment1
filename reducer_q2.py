#!/usr/bin/env python3
import sys
from collections import defaultdict

# Dictionary to store hour counts
hour_counts = defaultdict(int)

# Read input from the mapper
for line in sys.stdin:
    line = line.strip()
    hour, count = line.split("\t")
    
    # Sum up the counts for each hour
    hour_counts[hour] += int(count)

# Find the hour with the lowest flow
lowest_hour = None
lowest_flow = float('inf')

for hour, count in hour_counts.items():
    if count < lowest_flow:
        lowest_flow = count
        lowest_hour = hour

# Print the lowest hour and its flow count
if lowest_hour is not None:
    print(f"Lowest hourly flow: {lowest_flow} at hour {lowest_hour}")
