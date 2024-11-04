#!/usr/bin/env python3
import sys
from collections import defaultdict

counts = defaultdict(int)

for line in sys.stdin:
    print(f"DEBUG: Input to reducer - {line.strip()}", file=sys.stderr)

    line = line.strip()
    if line:  # Only process non-empty lines
        try:
            composite_key, count = line.split('\t')
            counts[composite_key] += int(count)
            print(f"DEBUG: Updated count for {composite_key} - {counts[composite_key]}", file=sys.stderr)
        except ValueError as e:
            print(f"DEBUG: Error processing line: {line} - {e}", file=sys.stderr)
            continue  # Skip to the next line if there's an error

# Find max and min counts
max_key, max_value = max(counts.items(), key=lambda item: item[1], default=(None, float('-inf')))
min_key, min_value = min(counts.items(), key=lambda item: item[1], default=(None, float('inf')))

# Print results
if max_key and min_key:
    print(f"Max Hourly Flow: {max_value} at {max_key}")
    print(f"Min Hourly Flow: {min_value} at {min_key}")
