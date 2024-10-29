# reducer.py
import sys
from collections import defaultdict
vehicle_counts = defaultdict(int)
total_count = 0
for line in sys.stdin:
    vehicle_type, count = line.strip().split("\t")
    count = int(count)
    vehicle_counts[vehicle_type] += count
    total_count += count
for vehicle_type, count in vehicle_counts.items():
    percentage = (count / total_count) * 100
    print(f"{vehicle_type}\t{percentage:.2f}%")
