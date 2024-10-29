# mapper.py
import sys
for line in sys.stdin:
    fields = line.strip().split(",")
    vehicle_type = fields[3]  # Assuming vehicle type is in 4th column
    print(f"{vehicle_type}\t1")
