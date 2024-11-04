#!/usr/bin/env python3

import sys

for line in sys.stdin:
    parts = line.strip().split(',')
    if len(parts) > 3:  # Ensure there are enough columns
        vehicle_type = parts[14]  # Adjust index based on your dataset
        print(f"{vehicle_type}\t1")  # Emit vehicle type and count
