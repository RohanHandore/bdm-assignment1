#!/usr/bin/env python3

import sys

total_speed = 0.0
count = 0

for line in sys.stdin:
    try:
        speed = float(line.strip())
        total_speed += speed
        count += 1
    except ValueError:
        continue  # Skip invalid values

if count > 0:
    average_speed = total_speed / count
    print(f"Average Speed of Motorbike: {average_speed:.2f}")
else:
    print("No valid motorbike speed data found.")
