#!/usr/bin/env python3

import sys
from collections import defaultdict

hourly_counts = defaultdict(int)

for line in sys.stdin:
    try:
        hour, count = line.strip().split('\t')
        count = int(count)  # Ensure count is an integer
        hourly_counts[hour] += count
    except ValueError as e:
        # Handle errors during count conversion or splitting
        print(f"Error processing line: {line.strip()} - {e}", file=sys.stderr)
    except Exception as e:
        # Handle any other unexpected errors
        print(f"Unexpected error processing line: {line.strip()} - {e}", file=sys.stderr)

# Find the highest and lowest counts safely
if hourly_counts:
    highest_hour = max(hourly_counts, key=hourly_counts.get)
    lowest_hour = min(hourly_counts, key=hourly_counts.get)

    print(f"Highest Hour: {highest_hour}, Count: {hourly_counts[highest_hour]}")
    print(f"Lowest Hour: {lowest_hour}, Count: {hourly_counts[lowest_hour]}")
else:
    print("No valid data found for processing.")
