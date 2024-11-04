#!/usr/bin/env python3
import sys

# Assume the structure of your CSV and adjust the indices accordingly
for line in sys.stdin:
    fields = line.strip().split(',')
    if len(fields) > 1:
        timestamp = fields[1]  # Timestamp
        vehicle_type = fields[4]  # Vehicle type
        if vehicle_type == 'Car':
            hour = timestamp.split(' ')[1].split(':')[0]  # Extract hour
            print(f"{hour}\t1")
