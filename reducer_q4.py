#!/usr/bin/env python3

import sys
from collections import defaultdict

lane_counts = defaultdict(int)

for input_line in sys.stdin:
    input_line = input_line.strip()
    if input_line:  # Only process non-empty lines
        try:
            lane_identifier, count_value = input_line.split('\t')
            lane_counts[lane_identifier] += int(count_value)  # Aggregate counts
        except ValueError as error_message:
            print(f"Error processing line: {input_line} - {error_message}", file=sys.stderr)
            continue  # Skip to the next line if there's an error

# Sort lanes by count and take top 10
top_lanes = sorted(lane_counts.items(), key=lambda item: item[1], reverse=True)[:10]

# Print the results
for lane, count in top_lanes:
    print(f"{lane}\t{count}")
