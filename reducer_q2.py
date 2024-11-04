#!/usr/bin/env python3
import sys

def main():
    current_key = None
    current_count = 0
    flow_data = {}  # For storing flow data

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        parts = line.split('\t')
        
        if len(parts) != 3:
            continue
        
        key, value = parts[0], int(parts[2])
        
        # Count flow data
        if key == "flow":
            hour = parts[1]
            flow_data[hour] = flow_data.get(hour, 0) + value
        elif key == "usage":
            current_key = parts[1]
            current_count += value

    # Output the collected flow data
    if flow_data:
        for hour, count in flow_data.items():
            print(f"Hour: {hour}, Count: {count}")
    else:
        print("No flow data available.")

    # Output the usage data if any
    if current_key:
        print(f"Usage Data: {current_key} -> {current_count}")

if __name__ == "__main__":
    main()
