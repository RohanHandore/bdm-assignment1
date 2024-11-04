#!/usr/bin/env python3

import sys
from collections import defaultdict

counts = defaultdict(int)

# Count occurrences of each location
for line in sys.stdin:
    line = line.strip()
    if line:
        lane_name, count = line.split('\t')
        counts[lane_name] += int(count)

# Sort locations by count and take top 10
top_locations = sorted(counts.items(), key=lambda item: item[1], reverse=True)[:10]

# Print the results
print("Top 10 Locations with Highest HGV Counts:")
for location, count in top_locations:
    print(f"{location}: {count}")
