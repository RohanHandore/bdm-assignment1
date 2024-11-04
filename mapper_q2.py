#!/usr/bin/env python3
import sys

# Read input line by line
for line in sys.stdin:
    line = line.strip()
    
    # Split the line by commas
    parts = line.split(",")
    
    # Check for the right number of parts
    if len(parts) < 16:
        print(f"Error processing line: {line}", file=sys.stderr)
        continue

    try:
        junction_number = int(parts[12])  # Junction number is at index 12
        vehicle_type = parts[14]           # Vehicle type is at index 14
        hour = int(parts[4])               # Hour is at index 4
        count = int(parts[15]) if parts[15].isdigit() else 0  # Count is at index 15
        
        # Filter for cars and M50 junctions (between 3 and 17)
        if vehicle_type == "CAR" and 3 <= junction_number <= 17:
            # Output key-value pair: (hour, junction_number) => count
            print(f"{hour},{junction_number}\t{count}")

    except Exception as e:
        print(f"Error processing line: {line} - {e}", file=sys.stderr)
