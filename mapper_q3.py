#!/usr/bin/env python3

import sys

line_count = 0  # Counter for the first three lines

for line in sys.stdin:
    line_count += 1
    if line_count <= 3:  # Print the first three lines
        print(f"Input Line {line_count}: {line.strip()}")

    # Strip leading/trailing whitespace and handle potential quotes
    line = line.strip().replace('"', '').replace("'", "")
    parts = [part.strip() for part in line.split(',')]

    # Check if there are enough columns
    if len(parts) > 19:  # Ensure there are enough columns
        vehicle_type = parts[14]  # Vehicle type should be at index 14
        speed = parts[19]          # Speed should be at index 19
        
        if vehicle_type == "MBIKE":  # Check if the vehicle is a motorbike
            try:
                speed_value = float(speed)  # Convert speed to float
                print(f"motorbike\t1\t{speed_value}")  # Emit count of 1 and speed
            except ValueError:
                print(f"Warning: Invalid speed value '{speed}' in line: {line.strip()}")
    else:
        print(f"Warning: Not enough columns in line: {line.strip()}")
