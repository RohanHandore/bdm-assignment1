#!/usr/bin/env python3
import sys

# Debug: to check if mapper is reading input correctly
print("Debug: Starting mapper...", file=sys.stderr)

for line in sys.stdin:
    try:
        print(f"Debug: Processing line: {line.strip()}", file=sys.stderr)
        fields = line.strip().split(',')
        
        # Check if the line has enough fields
        if len(fields) >= 14:
            cosit = fields[0].strip('"')
            junction_number = int(cosit[7:9])  # Extracting junction number from 'cosit'
            vehicle_class = fields[14].strip().upper()
            hour = int(fields[4].strip('"'))
            
            if 3 <= junction_number <= 17 and vehicle_class == "CAR":
                print(f"{hour}\t1")
            else:
                print(f"Debug: Skipped line due to junction or vehicle class: {line.strip()}", file=sys.stderr)
        else:
            print(f"Debug: Line has insufficient fields: {line.strip()}", file=sys.stderr)
    except Exception as e:
        print(f"Debug: Error processing line '{line.strip()}': {e}", file=sys.stderr)
