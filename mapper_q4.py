#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip().replace('"', '').replace("'", "")
    parts = [part.strip() for part in line.split(',')]
    
    # Check if the number of parts is at least what we expect
    if len(parts) > 14:  # Adjust this as needed for your CSV
        vehicle_type = parts[14]  # Vehicle type index
        lane_name = parts[12]      # Lane name index

        if vehicle_type in ["HGV_RIG", "HGV_ART"]:  # Check for HGV types
            print(f"{lane_name}\t1")  # Emit lane name with count 1
    else:
        print(f"Line skipped due to insufficient fields: {line}", file=sys.stderr)
