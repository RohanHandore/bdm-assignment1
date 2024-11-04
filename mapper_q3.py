#!/usr/bin/env python3

import sys

for line in sys.stdin:
    parts = line.strip().split(',')
    if len(parts) > 19:  # Ensure there are enough columns
        vehicle_type = parts[14]  # Adjust index based on your dataset
        speed = parts[19]          # Speed is at index 19
        
        if vehicle_type.strip() == "MBIKE":  # Check if the vehicle is a motorbike
            try:
                speed_value = float(speed)  # Convert speed to float
                print(f"MBIKE\t{1}\t{speed_value}")  # Emit count of 1 and speed
            except ValueError:
                continue  # Skip if speed is not a valid float
