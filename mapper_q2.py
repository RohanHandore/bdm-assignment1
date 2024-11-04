#!/usr/bin/env python3
import sys

for input_line in sys.stdin:
    # Print the raw input line for debugging
    print(f"DEBUG: Raw input line - {input_line.strip()}", file=sys.stderr)

    input_line = input_line.strip().replace('"', '').replace("'", "")
    data_segments = [segment.strip() for segment in input_line.split(',')]
    
    if len(data_segments) > 14:  # Ensure there are enough columns for processing
        vehicle_category = data_segments[14]  # Vehicle type index
        detector_id = data_segments[0]        # Counter ID index
        time_hour = data_segments[4]          # Hour index

        print(f"DEBUG: Parsed values - Detector ID: {detector_id}, Vehicle Category: {vehicle_category}, Hour: {time_hour}", file=sys.stderr)

        try:
            # Convert detector ID to integer and check for 'CAR'
            detector_id = int(detector_id)
            if detector_id in {1113, 1500, 1501, 1502, 1503, 1504, 1505, 1506, 1507, 1508, 1509, 1812, 15010, 15011, 15012, 201081, 201082} and vehicle_category == 'CAR':
                combined_key = f"[Hour: {time_hour}, Detector ID: {detector_id}]"
                print(f"DEBUG: Emitting - {combined_key}\t1", file=sys.stderr)
                print(f"{combined_key}\t1")
        except ValueError:
            print(f"DEBUG: Invalid detector ID - {data_segments[0]}", file=sys.stderr)
