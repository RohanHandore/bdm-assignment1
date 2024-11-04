#!/usr/bin/env python3

import sys
from collections import defaultdict

counts = defaultdict(int)

for line in sys.stdin:
    line = line.strip()
    if line:  # Only process non-empty lines
        try:
            lane_name, count = line.split('\t')
            counts[lane_name] += int(count)  # Aggregate counts
        except ValueError as e:
            print(f"Error processing line: {line} - {e}", file=sys.stderr)
            continue  # Skip to the next line if there's an error

# Sort locations by count and take top 10
top_locations = sorted(counts.items(), key=lambda item: item[1], reverse=True)[:10]

# Print the results
for location, count in top_locations:
    print(f"{location}\t{count}")
