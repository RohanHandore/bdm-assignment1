#!/usr/bin/env python3

import sys

current_vehicle_type = None
current_count = 0
total_count = 0

for line in sys.stdin:
    vehicle_type, count = line.strip().split('\t')
    count = int(count)
    
    if current_vehicle_type == vehicle_type:
        current_count += count
    else:
        if current_vehicle_type:
            print(f"{current_vehicle_type}\t{current_count}")
        current_vehicle_type = vehicle_type
        current_count = count

    total_count += count

# Print the last vehicle type
if current_vehicle_type == vehicle_type:
    print(f"{current_vehicle_type}\t{current_count}")

# Print percentages
if total_count > 0:
    print(f"Total Count: {total_count}")
