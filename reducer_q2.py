#!/usr/bin/env python3
import sys

# Reducer for the four analyses
def main():
    usage_counts = {}
    flow_counts = {}
    speed_sum = {}
    speed_count = {}
    hgv_counts = {}

    for line in sys.stdin:
        line = line.strip()
        if not line:  # Skip empty lines
            continue
        
        parts = line.split('\t')
        key_type = parts[0]
        
        # Analysis 1: Vehicle usage counts
        if key_type == "usage":
            classname = parts[1]
            count = int(parts[2])
            if classname not in usage_counts:
                usage_counts[classname] = 0
            usage_counts[classname] += count

        # Analysis 2: Flow counts for Cars
        elif key_type == "flow":
            hour = parts[1]
            count = int(parts[2])
            if hour not in flow_counts:
                flow_counts[hour] = 0
            flow_counts[hour] += count

        # Analysis 3: Average speed of Motorbikes
        elif key_type == "speed":
            cosit = parts[1]
            speed = float(parts[2])
            if cosit not in speed_sum:
                speed_sum[cosit] = 0
                speed_count[cosit] = 0
            speed_sum[cosit] += speed
            speed_count[cosit] += 1

        # Analysis 4: HGV counts
        elif key_type == "hgv":
            cosit = parts[1]
            count = int(parts[2])
            if cosit not in hgv_counts:
                hgv_counts[cosit] = 0
            hgv_counts[cosit] += count

    # Output for vehicle usage percentages
    total_usage = sum(usage_counts.values())
    for classname, count in usage_counts.items():
        percentage = (count / total_usage) * 100 if total_usage > 0 else 0
        print(f"Vehicle type: {classname}, Usage: {percentage:.2f}%")

    # Output for hourly flows (highest and lowest)
    max_flow_hour = max(flow_counts, key=flow_counts.get)
    min_flow_hour = min(flow_counts, key=flow_counts.get)
    print(f"Highest flow hour for Cars: {max_flow_hour} with {flow_counts[max_flow_hour]} counts")
    print(f"Lowest flow hour for Cars: {min_flow_hour} with {flow_counts[min_flow_hour]} counts")

    # Output for average speed of Motorbikes
    for cosit, total_speed in speed_sum.items():
        average_speed = total_speed / speed_count[cosit] if speed_count[cosit] > 0 else 0
        print(f"Average speed of Motorbikes at {cosit}: {average_speed:.2f} km/h")

    # Output for HGV counts (top 10 locations)
    sorted_hgv_counts = sorted(hgv_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    for cosit, count in sorted_hgv_counts:
        print(f"HGV counts at {cosit}: {count}")

if __name__ == "__main__":
    main()
