#!/usr/bin/env python3

import sys

# Set of valid counter IDs between junctions 03 and 17
valid_counters = {
    "1113", "1500", "1501", "1502", "1503", "1504", "1505", "1506", "1507",
    "1508", "1509", "1812", "15010", "15011", "15012", "201081", "201082"
}

for line in sys.stdin:
    # Skip empty lines
    if not line.strip():
        continue

    parts = line.strip().split(',')

    # Check for header and skip it
    if parts[0].replace('"', '').strip().lower() == 'counter_id':
        continue

    if len(parts) > 14:
        try:
            # Extract and clean counter ID, vehicle class, and hour
            counter_id = parts[0].replace('"', '').strip()
            vehicle_class = parts[14].replace('"', '').strip()
            hour = parts[4].replace('"', '').strip()

            # Check if counter ID is valid and vehicle is a car
            if counter_id in valid_counters and vehicle_class == 'CAR':
                composite_key = f"{hour}\t{counter_id}"
                print(f"{composite_key}\t1")
        except ValueError:
            # Handle any parsing issues
            continue
