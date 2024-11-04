#!/usr/bin/env python3

import sys
from collections import defaultdict

counts = defaultdict(int)

# Count occurrences of each location
for line in sys.stdin:
    line = line.strip()
    if line:
        try:
            lane_name, count = line.split('\t')
            counts[lane_name] += int(count)
        except ValueError as e:
            print(f"Error processing line: {line} - {e}")  # Debug output

# Sort locations by count and take top 10
top_locations = sorted(counts.items(), key=lambda item: item[1], reverse=True)[:10]

# Print the results
print("Top 10 Locations with Highest HGV Counts:")
for location, count in top_locations:
    print(f"{location}: {count}")
