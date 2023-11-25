import re

string = input()
valid_locations = []
travel_points = 0
pattern = r'(=|\/)([A-Z][A-Za-z]{2,})\1'
matches = re.findall(pattern , string)
if matches:
    for match in matches:
        location = match[1]
        valid_locations.append(location)
        travel_points += len(location)
print(f"Destinations: {', '.join(valid_locations)}")
print(f"Travel Points: {travel_points}")
