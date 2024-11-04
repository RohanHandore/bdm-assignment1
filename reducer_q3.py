#!/usr/bin/env python3

import sys

current_vehicle_type = None
current_count = 0
total_speed = 0.0
line_count = 0  # Counter for the first three lines of processed data

for line in sys.stdin:
    line_count += 1
    if line_count <= 3:  # Print the first three lines
        print(f"Processed Line {line_count}: {line.strip()}")

    try:
        vehicle_type, count, speed = line.strip().split('\t')
        count = int(count)
        speed = float(speed)
    except ValueError as e:
        print(f"Error parsing line '{line.strip()}': {e}")
        continue  # Skip this line if parsing fails

    if current_vehicle_type == vehicle_type:
        current_count += count
        total_speed += speed
    else:
        if current_vehicle_type == "motorbike":
            # Calculate and print average speed for motorbikes
            if current_count > 0:
                average_speed = total_speed / current_count
                print(f"Average Speed of {current_vehicle_type.capitalize()}: {average_speed:.2f}")
        current_vehicle_type = vehicle_type
        current_count = count
        total_speed = speed

# Print the average speed for the last vehicle type if it was a motorbike
if current_vehicle_type == "motorbike" and current_count > 0:
    average_speed = total_speed / current_count
    print(f"Average Speed of {current_vehicle_type.capitalize()}: {average_speed:.2f}")
