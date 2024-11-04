#!/usr/bin/env python3

import sys
from collections import defaultdict

hourly_count = defaultdict(int)

# Read input from standard input (mapper output)
for line in sys.stdin:
    try:
        hour, count = line.strip().split("\t")
        count = int(count)
        hourly_count[hour] += count
    except ValueError as e:
        sys.stderr.write(f"Error parsing line '{line}': {e}\n")

# Find the highest and lowest hourly flow
if hourly_count:
    highest_hour = max(hourly_count, key=hourly_count.get)
    lowest_hour = min(hourly_count, key=hourly_count.get)

    # Print the highest and lowest hourly flows
    print(f"Highest Hourly Flow: Hour {highest_hour}, Count {hourly_count[highest_hour]}")
    print(f"Lowest Hourly Flow: Hour {lowest_hour}, Count {hourly_count[lowest_hour]}")
else:
    print("No valid data processed.")
