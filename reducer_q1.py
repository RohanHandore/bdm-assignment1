#!/usr/bin/env python3

import sys

previous_vehicle = None
vehicle_count = 0
aggregate_count = 0

for input_line in sys.stdin:
    vehicle_category, count_value = input_line.strip().split('\t')
    count_value = int(count_value)
    
    if previous_vehicle == vehicle_category:
        vehicle_count += count_value
    else:
        if previous_vehicle:
            print(f"{previous_vehicle}\t{vehicle_count}")
        previous_vehicle = vehicle_category
        vehicle_count = count_value

    aggregate_count += count_value

# Print the last vehicle type
if previous_vehicle == vehicle_category:
    print(f"{previous_vehicle}\t{vehicle_count}")

# Print total count
if aggregate_count > 0:
    print(f"Total Count: {aggregate_count}")
