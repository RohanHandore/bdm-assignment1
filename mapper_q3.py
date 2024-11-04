#!/usr/bin/env python3

import sys

for line in sys.stdin:
    try:
        # Split the line into columns
        parts = line.strip().split(',')
        
        # Ensure there are enough columns to avoid IndexError
        if len(parts) > 18:  # Adjust the number based on the total columns in your data
            classname = parts[14]  # Vehicle type (column O)
            speed = parts[18]  # Speed (column S)
            
            # Check if the vehicle type is 'MOTORBIKE' and speed is valid
            if classname == 'MOTORBIKE' and speed.isdigit():
                print(f"motorbike\t{speed}")
    except ValueError as e:
        print(f"Error processing line: {line.strip()} - {e}", file=sys.stderr)
    except IndexError as e:
        print(f"Index error processing line: {line.strip()} - {e}", file=sys.stderr)
    except Exception as e:
        print(f"Unexpected error processing line: {line.strip()} - {e}", file=sys.stderr)
