#!/usr/bin/env python

import sys
from collections import defaultdict

location_counts = defaultdict(int)

for line in sys.stdin:
    location, count = line.strip().split('\t')
    location_counts[location] += int(count)

# Sort locations by counts and print top 10
top_locations = sorted(location_counts.items(), key=lambda x: x[1], reverse=True)[:10]
for location, count in top_locations:
    print(f"{location}\t{count}")
