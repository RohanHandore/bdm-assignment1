#!/usr/bin/env python3
import sys

def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        fields = line.split('\t')  # Split by tab character

        # Ensure there are enough fields in the row
        if len(fields) < 20:
            print("Skipping line due to insufficient fields:", line)  # Debug output
            continue
        
        cosit = fields[0]           # Cosit
        year = fields[1]            # Year
        month = fields[2]           # Month
        day = fields[3]             # Day
        hour = fields[4]            # Hour
        minute = fields[5]          # Minute
        vehicle_type = fields[14]   # Vehicle type (assuming this is correct)
        classname = fields[15]      # Class name

        # Analysis 1: Count vehicle types
        if vehicle_type and classname:
            print(f"usage\t{classname}\t1")  # Emit vehicle type count
        
        # Analysis 2: Hourly flow for Cars on M50
        if vehicle_type == "CAR":
            print(f"flow\t{hour}\t1")  # Emit hourly flow for Cars

if __name__ == "__main__":
    main()
