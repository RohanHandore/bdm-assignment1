#!/usr/bin/env python3

import sys

for line in sys.stdin:
    # Strip whitespace and remove quotes
    line = line.strip().replace('"', '').replace("'", "")
    parts = [part.strip() for part in line.split('\t')]  # Using tab as a delimiter

    # Ensure there are enough columns for processing
    if len(parts) > 19:  # Adjust based on the actual number of columns
        vehicle_type = parts[14]  # 'class' (vehicle type)
        hour = parts[4]            # 'hour'
        count = parts[10]          # Assuming 'lane' is count

        # Filter for Cars
        if vehicle_type == "CAR":  # We are only interested in Cars
            try:
                count_value = int(count)  # Convert count to integer
                print(f"{hour}\t{count_value}")  # Output hour and count for reducer
            except ValueError:
                continue  # Skip lines with invalid count values
