#!/usr/bin/env python3
import sys

for line in sys.stdin:
    # Print the raw input line for debugging
    print(f"DEBUG: Raw input line - {line.strip()}", file=sys.stderr)

    line = line.strip().replace('"', '').replace("'", "")
    parts = [part.strip() for part in line.split(',')]
    
    if len(parts) > 14:  # Ensure there are enough columns for processing
        vehicle_type = parts[14]  # Vehicle type index
        counter_id = parts[0]     # Counter ID index
        hour = parts[4]           # Hour index

        print(f"DEBUG: Parsed values - Counter ID: {counter_id}, Vehicle Type: {vehicle_type}, Hour: {hour}", file=sys.stderr)

        try:
            # Convert counter ID to integer and check for 'CAR'
            counter_id = int(counter_id)
            if counter_id in {1113, 1500, 1501, 1502, 1503, 1504, 1505, 1506, 1507, 1508, 1509, 1812, 15010, 15011, 15012, 201081, 201082} and vehicle_type == 'CAR':
                composite_key = f"[Hour: {hour}, Counter ID: {counter_id}]"
                print(f"DEBUG: Emitting - {composite_key}\t1", file=sys.stderr)
                print(f"{composite_key}\t1")
        except ValueError:
            print(f"DEBUG: Invalid counter ID - {parts[0]}", file=sys.stderr)
