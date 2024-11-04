#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip().replace('"', '').replace("'", "")
    parts = [part.strip() for part in line.split(',')]
    
    # Ensure there are enough columns for processing
    if len(parts) > 19:  # Adjust based on the actual number of columns
        vehicle_type = parts[14]  # Vehicle type index (assuming it is at index 14)
        lane_name = parts[12]      # Lane name index (assuming it is at index 12)

        # Check if the vehicle is HGV (both RIGID and HGV_ART)
        if vehicle_type in ["HGV_RIG", "HGV_ART"]:
            print(f"{lane_name}\t1")  # Emit lane name with count 1
        else:
            # Debug output: print vehicle type for non-HGVs
            print(f"Skipped vehicle type: {vehicle_type}")
    else:
        print("Not enough data in line:", line)  # Debug for bad data
