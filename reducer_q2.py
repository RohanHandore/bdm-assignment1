#!/usr/bin/env python3

import sys
from collections import defaultdict

# Dictionary to store counts of cars per hour
hour_counts = defaultdict(int)

# Read input from the mapper
for line in sys.stdin:
    line = line.strip()
    if line:
        try:
            hour, count = line.split('\t')
            hour_counts[hour] += int(count)  # Aggregate counts
        except ValueError as e:
            print(f"Error processing line: {line} - {e}", file=sys.stderr)
            continue  # Skip to the next line if there's an error

# Find the hour with the lowest flow
lowest_hour = None
lowest_flow = float('inf')

for hour, count in hour_counts.items():
    if count < lowest_flow:
        lowest_flow = count
        lowest_hour = hour

# Print the hour with the lowest flow and its count
if lowest_hour is not None:
    print(f"Lowest hourly flow: {lowest_flow} at hour {lowest_hour}")
else:
    print("No data available for the specified criteria.")
