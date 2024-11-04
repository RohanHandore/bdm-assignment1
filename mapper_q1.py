#!/usr/bin/env python3

import sys

for input_line in sys.stdin:
    data_columns = input_line.strip().split(',')
    if len(data_columns) > 3:  # Ensure there are enough columns
        vehicle_category = data_columns[14]  # Adjust index based on your dataset
        print(f"{vehicle_category}\t1")  # Emit vehicle type and count
