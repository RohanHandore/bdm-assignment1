#!/usr/bin/env python3
import sys

def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        fields = line.split('\t')

        # Check if the fields list is long enough
        if len(fields) < 20:
            print("Skipping line due to insufficient fields:", line)  # Debug output
            continue
        
        vehicle_type = fields[14]  # Make sure to check this index

        # Analysis 1: Count vehicle types
        if vehicle_type:
            print(f"Vehicle Type: {vehicle_type}")  # Debug output
            if vehicle_type.strip() == "CAR":
                print(f"flow\t{fields[4]}\t1")  # Emit hourly flow for Cars
            else:
                print(f"usage\t{fields[15]}\t1")  # Emit vehicle type count

if __name__ == "__main__":
    main()
