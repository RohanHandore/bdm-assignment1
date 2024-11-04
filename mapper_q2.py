#!/usr/bin/env python3

import sys

for line in sys.stdin:
    parts = line.strip().split(',')
    if len(parts) > 14:  # Ensure there are enough columns
        hour = parts[4]  # Assuming the 'hour' column is at index 4
        classname = parts[14]  # Vehicle type column
        cosit = parts[0]  # Counter site code column
        
        # Check if the vehicle type is 'CAR' and the location is on M50 (adjust 'cosit' range for junctions 03-17)
        if classname == 'CAR' and 997 <= int(cosit) <= 1011:  # Replace with the range for M50 junctions
            print(f"{hour}\t1")
