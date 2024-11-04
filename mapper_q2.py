#!/usr/bin/env python3

import sys

for line in sys.stdin:
    try:
        parts = line.strip().split(',')
        
        # Ensure there are enough columns to avoid IndexError
        if len(parts) > 14:
            hour = parts[4]  # Assuming the 'hour' column is at index 4
            classname = parts[14]  # Vehicle type column
            cosit = parts[0]  # Counter site code column

            # Check if 'cosit' and 'hour' are valid integers
            if classname == 'CAR' and 997 <= int(cosit) <= 1011:
                print(f"{hour}\t1")
    except ValueError as e:
        # Handle conversion errors or unexpected value formats
        print(f"Error processing line: {line.strip()} - {e}", file=sys.stderr)
    except IndexError as e:
        # Handle cases where indices are out of range
        print(f"Index error processing line: {line.strip()} - {e}", file=sys.stderr)
    except Exception as e:
        # Handle any other unexpected errors
        print(f"Unexpected error processing line: {line.strip()} - {e}", file=sys.stderr)
