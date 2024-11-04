#!/usr/bin/env python3
import sys

def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        fields = line.split('\t')  # Split by tab character

        if len(fields) < 20:  # Ensure enough fields are present
            continue
        
        cosit = fields[0]
        hour = fields[4]
        vehicle_type = fields[14]
        speed = fields[17]
        classname = fields[15]

        # Analysis 1: Count vehicle types
        if vehicle_type and classname:
            print(f"usage\t{classname}\t1")  # Emit vehicle type count
        
        # Analysis 2: Hourly flow for Cars on M50
        if vehicle_type == "CAR":
            print(f"flow\t{hour}\t1")  # Emit hourly flow for Cars

        # Analysis 3: Average speed of Motorbikes
        if classname == "MOTORBIKE":
            if speed:  # Check if speed is present
                print(f"speed\t{cosit}\t{speed}")

        # Analysis 4: Count HGVs
        if classname in ["HGV_RIG", "HGV_ART"]:
            print(f"hgv\t{cosit}\t1")

if __name__ == "__main__":
    main()
