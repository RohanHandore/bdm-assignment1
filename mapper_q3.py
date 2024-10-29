#!/usr/bin/env python

import sys

for line in sys.stdin:
    parts = line.strip().split(',')
    if len(parts) > 5:  # Ensure there are enough columns
        vehicle_type = parts[3]  # Vehicle type
        speed = parts[5]  # Assuming speed is in this index

        if vehicle_type == 'Motorbike':
            print(f"motorbike\t{speed}")  # Emit speed for motorbikes
