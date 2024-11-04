#!/usr/bin/env python3

import sys

for input_line in sys.stdin:
    # Strip whitespace and remove quotes
    input_line = input_line.strip().replace('"', '').replace("'", "")
    data_fields = [field.strip() for field in input_line.split(',')]
    
    # Ensure there are enough columns for processing
    if len(data_fields) > 19:  # Adjust based on the actual number of columns
        vehicle_category = data_fields[14]  # Adjust index based on your data
        speed_data = data_fields[18]        # Adjust index based on your data

        if vehicle_category == "MBIKE":  # Filter for motorbikes
            try:
                speed_value = float(speed_data)  # Convert speed to float
                print(speed_value)  # Print speed for reducer
            except ValueError:
                continue  # Skip lines with invalid speed values
