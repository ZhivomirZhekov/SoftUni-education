# Input
degrees = int(input())
time_of_day = input()
outfit = ''
shoes = ''
# Logic
if time_of_day == 'Morning':
    if 10 <= degrees <= 18:
        outfit = 'Sweatshirt'
        shoes = 'Sneakers'
    elif degrees >= 25:
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    else:
        outfit = 'Shirt'
        shoes = 'Moccasins'
elif time_of_day == 'Afternoon':
    if 10 <= degrees <= 18:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif degrees >= 25:
        outfit = 'Swim Suit'
        shoes = 'Barefoot'
    else:
        outfit = 'T-Shirt'
        shoes = 'Sandals'
else: #Evening
    outfit = 'Shirt'
    shoes = 'Moccasins'


# Output
print(f'It\'s {degrees} degrees, get your {outfit} and {shoes}.')