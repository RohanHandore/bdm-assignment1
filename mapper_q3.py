#!/usr/bin/env python3
import sys

def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        fields = line.split('\t')

        # Ensure we have enough fields
        if len(fields) < 20:
            continue
        
        # Get vehicle type and speed
        vehicle_type = fields[15]  # classname is at index 15
        speed = fields[19]          # speed is at index 19

        # Only consider motorbikes
        if vehicle_type.strip() == "MOTORBIKE":
            try:
                speed_value = float(speed)
                print(f"motorbike_speed\t1\t{speed_value}")  # Emit count and speed for motorbikes
            except ValueError:
                continue  # Skip any lines where speed is not a valid float

if __name__ == "__main__":
    main()
