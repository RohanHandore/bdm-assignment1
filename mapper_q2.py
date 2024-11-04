#!/usr/bin/env python3

import sys

for line in sys.stdin:
    # Strip whitespace and remove quotes
    line = line.strip().replace('"', '').replace("'", "")
    parts = [part.strip() for part in line.split(',')]
    
    # Ensure there are enough columns for processing
    if len(parts) > 19:  # Adjust based on the actual number of columns
        vehicle_type = parts[14]  # Adjust index based on your data
        hour = parts[4]            # Assuming hour is at index 4
        count = parts[10]          # Assuming count is at index 10

        # Filter for Cars and the specified junctions
        if vehicle_type == "CAR" and "M50" in parts[13]:  # Adjust index based on your data
            try:
                count_value = int(count)  # Convert count to integer
                print(f"{hour}\t{count_value}")  # Output hour and count for reducer
            except ValueError:
                continue  # Skip lines with invalid count values
