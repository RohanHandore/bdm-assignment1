#!/usr/bin/env python3

import sys

for input_line in sys.stdin:
    input_line = input_line.strip().replace('"', '').replace("'", "")
    data_fields = [field.strip() for field in input_line.split(',')]
    
    # Check if the number of fields is at least what we expect
    if len(data_fields) > 14:  # Adjust this as needed for your CSV
        vehicle_category = data_fields[14]  # Vehicle type index
        lane_identifier = data_fields[12]    # Lane name index

        if vehicle_category in ["HGV_RIG", "HGV_ART"]:  # Check for HGV types
            print(f"{lane_identifier}\t1")  # Emit lane name with count 1
    else:
        print(f"Line skipped due to insufficient fields: {input_line}", file=sys.stderr)
