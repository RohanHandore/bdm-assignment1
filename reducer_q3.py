#!/usr/bin/env python3

import sys

current_vehicle_type = None
current_count = 0
total_speed = 0.0

for line in sys.stdin:
    vehicle_type, count, speed = line.strip().split('\t')
    count = int(count)
    speed = float(speed)

    if current_vehicle_type == vehicle_type:
        current_count += count
        total_speed += speed
    else:
        if current_vehicle_type == "MBIKE":
            # Calculate and print average speed for motorbikes
            if current_count > 0:
                average_speed = total_speed / current_count
                print(f"Average Speed of {current_vehicle_type.capitalize()}: {average_speed:.2f}")
        current_vehicle_type = vehicle_type
        current_count = count
        total_speed = speed

# Print the average speed for the last vehicle type if it was a motorbike
if current_vehicle_type == "MBIKE" and current_count > 0:
    average_speed = total_speed / current_count
    print(f"Average Speed of {current_vehicle_type.capitalize()}: {average_speed:.2f}")
