#!/usr/bin/env python3
import sys

# Debug: to check if reducer is starting
print("Debug: Starting reducer...", file=sys.stderr)

hourly_counts = {}

for line in sys.stdin:
    try:
        print(f"Debug: Processing line: {line.strip()}", file=sys.stderr)
        hour, count = line.strip().split('\t')
        hour = int(hour)
        count = int(count)
        
        if hour in hourly_counts:
            hourly_counts[hour] += count
        else:
            hourly_counts[hour] = count
    except Exception as e:
        print(f"Debug: Error processing line '{line.strip()}': {e}", file=sys.stderr)

# Finding the highest and lowest hourly flows
if hourly_counts:
    max_hour = max(hourly_counts, key=hourly_counts.get)
    min_hour = min(hourly_counts, key=hourly_counts.get)
    
    print(f"Highest Hourly Flow: Hour {max_hour} with {hourly_counts[max_hour]} cars")
    print(f"Lowest Hourly Flow: Hour {min_hour} with {hourly_counts[min_hour]} cars")
else:
    print("Debug: No data found in hourly counts.", file=sys.stderr)
