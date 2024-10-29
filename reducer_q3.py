#!/usr/bin/env python

import sys

total_speed = 0
count = 0

for line in sys.stdin:
    _, speed = line.strip().split('\t')
    total_speed += float(speed)
    count += 1

average_speed = total_speed / count if count > 0 else 0
print(f"Average Speed of Motorbikes: {average_speed}")
