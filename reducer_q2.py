#!/usr/bin/env python3

import sys

current_hour = None
hourly_counts = {}

for line in sys.stdin:
    hour, count = line.strip().split('\t')
    count = int(count)

    if hour in hourly_counts:
        hourly_counts[hour] += count
    else:
        hourly_counts[hour] = count

# Now calculate the highest and lowest hourly flows
if hourly_counts:
    highest_hour = max(hourly_counts, key=hourly_counts.get)
    lowest_hour = min(hourly_counts, key=hourly_counts.get)
    print(f"Highest Hourly Flow of Cars: {hourly_counts[highest_hour]} at hour {highest_hour}")
    print(f"Lowest Hourly Flow of Cars: {hourly_counts[lowest_hour]} at hour {lowest_hour}")
else:
    print("No valid car count data found.")
