# Input
day = int(input())
type_of_room = input()
rating = input()
nights = day - 1
price_per_night = 0
# Logic
if type_of_room == 'room for one person':
    price_per_night = 18
elif type_of_room == 'apartment':
    price_per_night = 25
    if nights < 10:
        price_per_night *= 0.7
    elif 10 <= nights <= 15:
        price_per_night *= 0.65
    else:
        price_per_night *= 0.5
elif type_of_room == 'president apartment':
    price_per_night = 35
    if nights < 10:
        price_per_night *= 0.9
    elif 10 <= nights <= 15:
        price_per_night *= 0.85
    else:
        price_per_night *= 0.8

if rating == 'positive':
    price_per_night *= 1.25
else:
    price_per_night *= 0.9
total = price_per_night * nights
# Output
print(f'{total:.2f}')