# Input
budged_group = int(input())
season = input()
number_fishermen = int(input())
boat_rent = 0
# Logic
if season == 'Spring':
    boat_rent = 3000
    if number_fishermen <= 6:
        boat_rent *= 0.9
    elif 7 <= number_fishermen <= 11:
        boat_rent *= 0.85
    elif number_fishermen >= 12:
        boat_rent *= 0.75
elif season == 'Summer':
    boat_rent = 4200
    if number_fishermen <= 6:
        boat_rent *= 0.9
    elif 7 <= number_fishermen <= 11:
        boat_rent *= 0.85
    elif number_fishermen >= 12:
        boat_rent *= 0.75
elif season == 'Autumn':
    boat_rent = 4200
    if number_fishermen <= 6:
        boat_rent *= 0.9
    elif 7 <= number_fishermen <= 11:
        boat_rent *= 0.85
    elif number_fishermen >= 12:
        boat_rent *= 0.75
elif season == 'Winter':
    boat_rent = 2600
    if number_fishermen <= 6:
        boat_rent *= 0.9
    elif 7 <= number_fishermen <= 11:
        boat_rent *= 0.85
    elif number_fishermen >= 12:
        boat_rent *= 0.75
if number_fishermen % 2 == 0:
    if season != 'Autumn':
        boat_rent *= 0.95
difference = abs(budged_group - boat_rent)
if budged_group >= boat_rent:
    print(f'Yes! You have {difference:.2f} leva left.')
else:
    print(f'Not enough money! You need {difference:.2f} leva.')
# Output
