# Reducer for Vehicle Type Percentage Calculation
import sys

vehicle_count = {}
total_count = 0

for line in sys.stdin:
    vehicle_type, count = line.strip().split("\t")
    count = int(count)
    total_count += count
    if vehicle_type in vehicle_count:
        vehicle_count[vehicle_type] += count
    else:
        vehicle_count[vehicle_type] = count

# Calculate and output the percentage of each vehicle type
for vehicle_type in vehicle_count:
    percentage = (vehicle_count[vehicle_type] / total_count) * 100
    print(f"{vehicle_type}\t{percentage:.2f}%")
