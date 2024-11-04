#!/usr/bin/env python3

import sys

for line in sys.stdin:
    # Strip whitespace and remove quotes
    line = line.strip().replace('"', '').replace("'", "")
    parts = [part.strip() for part in line.split(',')]
    
    # Ensure there are enough columns for processing
    if len(parts) > 19:  # Adjust based on the actual number of columns
        vehicle_type = parts[14]  # Adjust index based on your data
        lane_name = parts[12]      # Adjust index based on your data
        
        # Check if the vehicle is HGV (both RIGID and ART)
        if vehicle_type in ["RIGID", "ART"]:
            print(f"{lane_name}\t1")  # Emit lane name with count 1
