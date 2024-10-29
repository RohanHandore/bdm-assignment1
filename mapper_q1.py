#!/usr/bin/env python

import sys

for line in sys.stdin:
    parts = line.strip().split(',')
    if len(parts) > 3:  # Ensure there are enough columns
        vehicle_type = parts[3]  # Adjust index based on your dataset
        print(f"{vehicle_type}\t1")  # Emit vehicle type and count
