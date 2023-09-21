# Input
from math import floor
record_in_seconds = float(input())
distance_in_meters = float(input())
time_in_seconds_swimming_1meter = float(input())

# Logic

time_for_full_distance = distance_in_meters * time_in_seconds_swimming_1meter
time_with_delay = floor(distance_in_meters / 15)
full_delay = time_with_delay * 12.5

full_time = time_for_full_distance + full_delay

if record_in_seconds > full_time:
    print(f'Yes, he succeeded! The new world record is {full_time:.2f} seconds.')

else:
    print(f'No, he failed! He was {full_time - record_in_seconds:.2f} seconds slower.')


