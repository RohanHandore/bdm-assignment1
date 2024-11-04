#!/usr/bin/env python3

import sys

hourly_counts = {}

for line in sys.stdin:
    line = line.strip()
    if line:  # Only process non-empty lines
        try:
            hour, count = line.split('\t')
            count = int(count)
            if hour in hourly_counts:
                hourly_counts[hour] += count  # Aggregate counts
            else:
                hourly_counts[hour] = count
        except ValueError as e:
            print(f"Error processing line: {line} - {e}", file=sys.stderr)
            continue  # Skip to the next line if there's an error

# Find the highest and lowest hourly flows
if hourly_counts:
    highest_hour = max(hourly_counts.items(), key=lambda item: item[1])
    lowest_hour = min(hourly_counts.items(), key=lambda item: item[1])

    print(f"Highest flow: Hour: {highest_hour[0]}, Count: {highest_hour[1]}")
    print(f"Lowest flow: Hour: {lowest_hour[0]}, Count: {lowest_hour[1]}")
else:
    print("No data processed.")
