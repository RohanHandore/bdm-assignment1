#!/usr/bin/env python3
import sys
from collections import defaultdict

# Dictionary to hold the lowest counts for each hour
lowest_flows = {}

# Read input line by line
for line in sys.stdin:
    line = line.strip()
    hour_junction, count = line.split("\t")
    hour, junction = hour_junction.split(",")
    
    # Convert hour and junction to integers
    hour = int(hour)
    junction = int(junction)
    count = int(count)

    # Check if this hour is already in lowest_flows
    if hour not in lowest_flows:
        lowest_flows[hour] = (junction, count)
    else:
        # Compare with current lowest count
        if count < lowest_flows[hour][1]:
            lowest_flows[hour] = (junction, count)

# Output the lowest hourly flows
print("Lowest Hourly Flows for Cars on M50:")
for hour, (junction, count) in sorted(lowest_flows.items()):
    print(f"Hour: {hour}, Junction: {junction}, Count: {count}")
