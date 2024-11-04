#!/usr/bin/env python3

import sys

def parse_line(line):
    try:
        fields = line.strip().split(",")
        if len(fields) > 14:
            # Extract relevant fields: junction, vehicle type, and hour
            junction = int(fields[0].strip('"'))
            vehicle_type = fields[14].strip('"')  # Column for vehicle type
            hour = fields[4].strip('"')  # Column for hour

            # Debug: Print the parsed fields for inspection
            sys.stderr.write(f"Parsed fields - Junction: {junction}, Vehicle Type: {vehicle_type}, Hour: {hour}\n")

            # Check if the record is for cars and between junctions 03-17
            if 3 <= junction <= 17 and vehicle_type == 'CAR':
                # Emit the hour and count of 1 for the vehicle
                print(f"{hour}\t1")
    except (ValueError, IndexError) as e:
        sys.stderr.write(f"Error parsing line '{line}': {e}\n")

# Read input from standard input
for line in sys.stdin:
    parse_line(line)
