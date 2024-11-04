import sys

def parse_line(line):
    fields = line.strip().split(",")
    if len(fields) > 12:
        try:
            # Extract relevant fields: junction, vehicle type, and time
            junction = int(fields[0].strip('"'))
            vehicle_type = fields[14].strip('"')  # Column that indicates vehicle type
            hour = fields[4].strip('"')  # Column that indicates the hour

            # Check if the record is for cars and is between junctions 03-17
            if 3 <= junction <= 17 and vehicle_type == 'CAR':
                # Emit the hour and count of 1 for the vehicle
                print(f"{hour}\t1")
        except ValueError:
            pass  # Ignore invalid lines

for line in sys.stdin:
    parse_line(line)
