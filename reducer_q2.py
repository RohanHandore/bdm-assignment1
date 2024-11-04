#!/usr/bin/env python3
import sys

def main():
    usage_counts = {}
    flow_counts = {}

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        parts = line.split('\t')
        key_type = parts[0]
        
        # Analysis 1: Vehicle usage counts
        if key_type == "usage":
            classname = parts[1]
            count = int(parts[2])
            usage_counts[classname] = usage_counts.get(classname, 0) + count

        # Analysis 2: Flow counts for Cars
        elif key_type == "flow":
            hour = parts[1]
            count = int(parts[2])
            flow_counts[hour] = flow_counts.get(hour, 0) + count

    # Output for vehicle usage percentages
    total_usage = sum(usage_counts.values())
    for classname, count in usage_counts.items():
        percentage = (count / total_usage) * 100 if total_usage > 0 else 0
        print(f"Vehicle type: {classname}, Usage: {percentage:.2f}%")

    # Output for hourly flows (highest and lowest)
    if flow_counts:
        max_flow_hour = max(flow_counts, key=flow_counts.get)
        min_flow_hour = min(flow_counts, key=flow_counts.get)
        print(f"Highest flow hour for Cars: {max_flow_hour} with {flow_counts[max_flow_hour]} counts")
        print(f"Lowest flow hour for Cars: {min_flow_hour} with {flow_counts[min_flow_hour]} counts")
    else:
        print("No flow data available.")  # Debug output

if __name__ == "__main__":
    main()
