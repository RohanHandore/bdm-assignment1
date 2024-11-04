import sys

hourly_count = {}

# Read input line-by-line from the mapper output
for line in sys.stdin:
    hour, count = line.strip().split("\t")
    count = int(count)

    if hour in hourly_count:
        hourly_count[hour] += count
    else:
        hourly_count[hour] = count

# Find the highest and lowest hourly flow
highest_hour = max(hourly_count, key=hourly_count.get)
lowest_hour = min(hourly_count, key=hourly_count.get)

# Print the highest and lowest hourly flows
print(f"Highest Hourly Flow: Hour {highest_hour}, Count {hourly_count[highest_hour]}")
print(f"Lowest Hourly Flow: Hour {lowest_hour}, Count {hourly_count[lowest_hour]}")
