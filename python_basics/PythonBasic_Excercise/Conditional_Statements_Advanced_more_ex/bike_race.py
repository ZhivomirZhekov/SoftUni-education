# Input
number_juniors = int(input())
number_seniors = int(input())
type_race = input()
charity = 0
# Logic
total_participants = number_seniors + number_juniors
if type_race == 'trail':
    if total_participants >= 50:
        charity = number_juniors * 5.5 + number_seniors * 7
    else:
        charity = (number_juniors * 5.5 + number_seniors * 7)
elif type_race == 'cross-country':
    if total_participants >= 50:
        charity = (number_juniors * 8+ number_seniors * 9.5) * 0.75
    else:
        charity = (number_juniors * 8 + number_seniors * 9.5)
elif type_race == 'downhill':
    if total_participants >= 50:
        charity = (number_juniors * 12.25 + number_seniors * 13.75)
    else:
        charity = (number_juniors * 12.25 + number_seniors * 13.75)
elif type_race == 'road':
    if total_participants >= 50:
        charity = (number_juniors * 20 + number_seniors * 21.50)
    else:
        charity = (number_juniors * 20 + number_seniors * 21.5)
total = charity * 0.95
# Output
print(f'{total:.2f}')