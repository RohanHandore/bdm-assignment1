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
        
        # Get vehicle type
        vehicle_type = fields[15]  # classname is at index 15
        
        # Count vehicle types
        if vehicle_type.strip() == "CAR":
            hour = fields[4]  # hour is at index 4
            print(f"flow\t{hour}\t1")  # Emit hourly flow for Cars
        else:
            print(f"usage\t{vehicle_type.strip()}\t1")  # Emit vehicle type count

if __name__ == "__main__":
    main()
