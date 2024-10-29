#!/usr/bin/env python3
import sys

current_word = None
current_count = 0

# Read each line from the input
for line in sys.stdin:
    word, count = line.strip().split("\t")  # Split the input into word and count
    count = int(count)  # Convert count to an integer

    if current_word == word:  # If the same word is encountered
        current_count += count  # Sum the counts
    else:
        if current_word:  # Output the previous word's count
            print(f"{current_word}\t{current_count}")
        current_word = word  # Switch to the new word
        current_count = count  # Set the count for the new word

# Output the last word's count
if current_word == word:
    print(f"{current_word}\t{current_count}")
