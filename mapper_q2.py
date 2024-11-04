#!/usr/bin/env python3

import sys

# Define junctions
start_junction = 3
end_junction = 17

for line in sys.stdin:
    line = line.strip().replace('"', '').replace("'", "")
    parts = [part.strip() for part in line.split(',')]

    # Check if we have enough parts to process
    if len(parts) > 14:  # Adjust according to your CSV
        junction_number = int(parts[12])  # Assuming lane name is at index 12
        vehicle_type = parts[14]  # Assuming vehicle type is at index 14
        hour = parts[4]  # Assuming hour is at index 4
        count = int(parts[15]) if len(parts) > 15 and parts[15].isdigit() else 0  # Assuming count is at index 15

        # Filter for cars and within specified junctions
        if vehicle_type == "CAR" and start_junction <= junction_number <= end_junction:
            print(f"{hour}\t{count}")  # Emit hour and count
    else:
        print(f"Line skipped due to insufficient fields: {line}", file=sys.stderr)
