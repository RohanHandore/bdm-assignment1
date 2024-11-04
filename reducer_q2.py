#!/usr/bin/env python3

import sys

current_hour = None
current_count = 0
hourly_counts = []

for line in sys.stdin:
    hour, count = line.strip().split('\t')
    count = int(count)
    
    if current_hour == hour:
        current_count += count
    else:
        if current_hour:
            hourly_counts.append(current_count)
        current_hour = hour
        current_count = count

# Append the last hour count
if current_hour is not None:
    hourly_counts.append(current_count)

# Calculate highest and lowest hourly flows
if hourly_counts:
    highest_flow = max(hourly_counts)
    lowest_flow = min(hourly_counts)
    print(f"Highest Hourly Flow of Cars: {highest_flow}")
    print(f"Lowest Hourly Flow of Cars: {lowest_flow}")
else:
    print("No valid car count data found.")
