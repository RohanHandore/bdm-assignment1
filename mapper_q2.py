#!/usr/bin/env python3

import sys

for line in sys.stdin:
    try:
        # Split the line into columns
        parts = line.strip().split(',')
        
        # Ensure there are enough columns to avoid IndexError
        if len(parts) > 14:
            cosit = int(parts[0])  # Counter site code (column A)
            hour = parts[4]  # Hour (column E)
            classname = parts[14]  # Vehicle type (column O)
            
            # Check if the 'classname' is 'CAR' and 'cosit' is within the M50 range (junctions 03-17)
            if classname == 'CAR' and 997 <= cosit <= 1011:  # Adjust cosit range if needed
                print(f"{hour}\t1")
    except ValueError as e:
        print(f"Error processing line: {line.strip()} - {e}", file=sys.stderr)
    except IndexError as e:
        print(f"Index error processing line: {line.strip()} - {e}", file=sys.stderr)
    except Exception as e:
        print(f"Unexpected error processing line: {line.strip()} - {e}", file=sys.stderr)
