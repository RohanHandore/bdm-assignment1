#!/usr/bin/env python

import sys

for line in sys.stdin:
    parts = line.strip().split(',')
    if len(parts) > 2:  # Adjust index based on your dataset
        lane = parts[2]  # Assuming this is the lane number or similar
        hour = parts[1].split(':')[0]  # Extract the hour from a timestamp
        vehicle_type = parts[3]  # Vehicle type
        
        if vehicle_type == 'Car' and 'M50' in lane:  # Change condition as necessary
            print(f"{hour}\t1")
