#!/usr/bin/env python3
import sys

# Read each line from the input
for line in sys.stdin:
    # Strip leading/trailing whitespace and split the line into words
    words = line.strip().split()
    # Emit each word with a count of 1
    for word in words:
        print(f"{word}\t1")
