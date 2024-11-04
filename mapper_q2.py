#!/usr/bin/env python3

import sys

# Read input line by line
for line in sys.stdin:
    # Strip whitespace and split by comma
    parts = line.strip().split(',')
    
    # Ensure there are enough columns for processing
    if len(parts) > 4:  # Adjust based on the number of columns
        hour = parts[4]  # Hour index (column 4)
        vehicle_type = parts[14]  # Vehicle type index (class column)
        lane_name = parts[11]  # Lane name index (lanename column)

        # Check if the vehicle is a car and in the specified lane range
        if vehicle_type == "CAR" and ("Junction 3" in lane_name or "Junction 4" in lane_name or
                                       "Junction 5" in lane_name or "Junction 6" in lane_name or
                                       "Junction 7" in lane_name or "Junction 8" in lane_name or
                                       "Junction 9" in lane_name or "Junction 10" in lane_name or
                                       "Junction 11" in lane_name or "Junction 12" in lane_name or
                                       "Junction 13" in lane_name or "Junction 14" in lane_name or
                                       "Junction 15" in lane_name or "Junction 16" in lane_name or
                                       "Junction 17" in lane_name):
            # Emit hour and count of 1
            print(f"{hour}\t1")
