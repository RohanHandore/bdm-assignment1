#!/usr/bin/env python3
import sys
from collections import defaultdict

flow_counts = defaultdict(int)

for input_line in sys.stdin:
    print(f"DEBUG: Input to reducer - {input_line.strip()}", file=sys.stderr)

    input_line = input_line.strip()
    if input_line:  # Only process non-empty lines
        try:
            key_combination, flow_count = input_line.split('\t')
            flow_counts[key_combination] += int(flow_count)
            print(f"DEBUG: Updated count for {key_combination} - {flow_counts[key_combination]}", file=sys.stderr)
        except ValueError as error_message:
            print(f"DEBUG: Error processing line: {input_line} - {error_message}", file=sys.stderr)
            continue  # Skip to the next line if there's an error

# Find max and min flow counts
max_combination, max_flow = max(flow_counts.items(), key=lambda item: item[1], default=(None, float('-inf')))
min_combination, min_flow = min(flow_counts.items(), key=lambda item: item[1], default=(None, float('inf')))

# Print results
if max_combination and min_combination:
    print(f"Max Hourly Flow: {max_flow} at {max_combination}")
    print(f"Min Hourly Flow: {min_flow} at {min_combination}")
