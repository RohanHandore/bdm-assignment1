#!/usr/bin/env python

import sys

for line in sys.stdin:
    parts = line.strip().split(',')
    if len(parts) > 3:  # Ensure there are enough columns
        vehicle_type = parts[14]  # Vehicle type
        location = parts[12]  # Assuming this is the location

        if vehicle_type in ['RIGID', 'HGV_ART']:  # Filter for HGV types
            print(f"{location}\t1")  # Emit location and count
