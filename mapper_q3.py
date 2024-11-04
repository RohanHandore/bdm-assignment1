#!/usr/bin/env python3

import sys

for line in sys.stdin:
    parts = line.strip().split(',')
    if len(parts) > 19:  # Ensure there are enough columns
        vehicle_type = parts[14]  # Adjust index based on your dataset
        speed = parts[19]          # Speed is at index 19
        
        # Debugging: Print the vehicle type and speed
        # print(f"DEBUG: Vehicle Type: {vehicle_type}, Speed: {speed}")  # Uncomment for debugging
        
        if vehicle_type.strip() == "MBIKE":  # Check if the vehicle is a motorbike
            try:
                speed_value = float(speed)  # Convert speed to float
                print(f"motorbike\t1\t{speed_value}")  # Emit count of 1 and speed
            except ValueError:
                # Uncomment for debugging if invalid speed is encountered
                # print(f"DEBUG: Invalid speed value: {speed}")  
                continue  # Skip if speed is not a valid float
