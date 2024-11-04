#!/usr/bin/env python3

import sys

cumulative_speed = 0.0
speed_count = 0

for input_line in sys.stdin:
    try:
        speed_value = float(input_line.strip())
        cumulative_speed += speed_value
        speed_count += 1
    except ValueError:
        continue  # Skip invalid values

if speed_count > 0:
    average_motorbike_speed = cumulative_speed / speed_count
    print(f"Average Speed of Motorbike: {average_motorbike_speed:.2f}")
else:
    print("No valid motorbike speed data found.")
