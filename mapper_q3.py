#!/usr/bin/env python3

import sys

line_count = 0  # Counter for the first three lines

for line in sys.stdin:
    line_count += 1
    if line_count <= 3:  # Print the first three lines
        print(f"Input Line {line_count}: {line.strip()}")

    parts = line.strip().split(',')
    if len(parts) > 19:  # Ensure there are enough columns
        vehicle_type = parts[14]  # Adjust index based on your dataset
        speed = parts[19]          # Speed is at index 19
        
        if vehicle_type.strip() == "MBIKE":  # Check if the vehicle is a motorbike
            try:
                speed_value = float(speed)  # Convert speed to float
                print(f"motorbike\t1\t{speed_value}")  # Emit count of 1 and speed
            except ValueError:
                continue  # Skip if speed is not a valid float
