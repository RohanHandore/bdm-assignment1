# Mapper for Vehicle Type Percentage Calculation
import sys

for line in sys.stdin:
    data = line.strip().split(",")
    # Extract the vehicle type (classname) from the correct index (14 for column O)
    vehicle_type = data[14]
    print(f"{vehicle_type}\t1")
