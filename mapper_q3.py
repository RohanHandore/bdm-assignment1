#!/usr/bin/env python3

import sys

for line in sys.stdin:
    # Strip whitespace and remove quotes
    line = line.strip().replace('"', '').replace("'", "")
    parts = [part.strip() for part in line.split(',')]
    
    # Ensure there are enough columns for processing
    if len(parts) > 19:  # Adjust based on the actual number of columns
        vehicle_type = parts[14]  # Adjust index based on your data
        speed = parts[20]         # Adjust index based on your data

        if vehicle_type == "MBIKE":  # Filter for motorbikes
            try:
                speed_value = float(speed)  # Convert speed to float
                print(speed_value)  # Print speed for reducer
            except ValueError:
                continue  # Skip lines with invalid speed values
