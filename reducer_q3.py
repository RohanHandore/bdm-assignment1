#!/usr/bin/env python3

import sys

total_speed = 0
motorbike_count = 0

for line in sys.stdin:
    try:
        _, speed = line.strip().split('\t')
        speed = float(speed)
        total_speed += speed
        motorbike_count += 1
    except ValueError as e:
        print(f"Error processing line: {line.strip()} - {e}", file=sys.stderr)
    except Exception as e:
        print(f"Unexpected error processing line: {line.strip()} - {e}", file=sys.stderr)

# Calculate and print the average speed
if motorbike_count > 0:
    average_speed = total_speed / motorbike_count
    print(f"Average Speed of Motorbikes: {average_speed:.2f}")
else:
    print("No valid motorbike data found for processing.")
#!/usr/bin/env python3
import sys

def main():
    current_count = 0
    total_speed = 0.0

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        parts = line.split('\t')
        
        if len(parts) != 3:
            continue
        
        key, count, speed = parts[0], int(parts[1]), float(parts[2])

        if key == "motorbike_speed":
            current_count += count
            total_speed += speed

    # Calculate and output the average speed for motorbikes
    if current_count > 0:
        average_speed = total_speed / current_count
        print(f"Average Speed of Motorbikes: {average_speed:.2f}")
    else:
        print("No motorbike data available.")

if __name__ == "__main__":
    main()
