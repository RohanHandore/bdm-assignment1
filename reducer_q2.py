#!/usr/bin/env python

import sys
from collections import defaultdict

hourly_counts = defaultdict(int)

for line in sys.stdin:
    hour, count = line.strip().split('\t')
    hourly_counts[hour] += int(count)

# Find highest and lowest
highest_hour = max(hourly_counts, key=hourly_counts.get)
lowest_hour = min(hourly_counts, key=hourly_counts.get)

print(f"Highest Hour: {highest_hour}, Count: {hourly_counts[highest_hour]}")
print(f"Lowest Hour: {lowest_hour}, Count: {hourly_counts[lowest_hour]}")
