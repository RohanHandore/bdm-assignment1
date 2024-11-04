#!/usr/bin/env python3
import sys

# Define the junctions for M50 between junction 03 and junction 17
junctions = ["3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17"]

# Read input line by line
for line in sys.stdin:
    line = line.strip()

    # Skip the header line
    if line.startswith("cosit"):
        continue

    # Split the line into columns
    columns = line.split("\t")
    
    # Extract the relevant columns
    try:
        hour = columns[4]  # hour column (index 4)
        lane_name = columns[11]  # lanename column (index 11)
        vehicle_class = columns[15]  # classname column (index 15)
        
        # Check if the vehicle is a car and the lane is in the M50 range
        if vehicle_class == "CAR" and any(f"Junction {junction}" in lane_name for junction in junctions):
            # Emit the hour with a count of 1
            print(f"{hour}\t1")
    except IndexError:
        continue
