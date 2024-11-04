#!/usr/bin/env python3

import sys
from collections import defaultdict

hourly_counts = defaultdict(int)

for line in sys.stdin:
    line = line.strip()
    if line:
        try:
            composite_key, count = line.rsplit('\t', 1)
            hourly_counts[composite_key] += int(count)
        except ValueError:
            continue  # Skip lines with parsing issues

# Initialize variables for min and max
min_count = float('inf')
max_count = float('-inf')
min_key = None
max_key = None

# Identify the min and max hourly flows
for key, count in hourly_counts.items():
    if count > max_count:
        max_count = count
        max_key = key
    if count < min_count:
        min_count = count
        min_key = key

# Print results
print("Lowest Hourly Flow:")
if min_key:
    print(f"{min_key}\t{min_count}")

print("Highest Hourly Flow:")
if max_key:
    print(f"{max_key}\t{max_count}")
