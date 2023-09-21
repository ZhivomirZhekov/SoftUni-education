# Input
mount = input()
number_nights = int(input())
studio = 0
apartment = 0
# Logic
if mount == 'May' or mount == 'October':
    if 14 > number_nights > 7: # 5% DISCOUNT STUDIO
        studio = 50 * number_nights * 0.95
        apartment = 65 * number_nights
    elif number_nights > 14: # 30% DISCOUNT STUDIO AND 10% APARTMENT
        studio = 50 * number_nights * 0.7
        apartment = 65 * number_nights * 0.9
    else:
        studio = 50 * number_nights
        apartment = 65 * number_nights
elif mount == 'June' or mount == 'September':
    if number_nights > 14:  # 20% DISCOUNT STUDIO AND 10% APARTMENT
        studio = 75.20 * number_nights * 0.8
        apartment = 68.70 * number_nights * 0.9
    else:
        studio = 75.20 * number_nights
        apartment = 68.70 * number_nights
elif mount == 'July' or mount == 'August':
    if number_nights > 14:
        studio = 76 * number_nights
        apartment = 77 * number_nights * 0.9 # 10% DISCOUNT
    else:
        studio = 76 * number_nights
        apartment = 77 * number_nights

# Output
print(f'Apartment: {apartment:.2f} lv.')
print(f'Studio: {studio:.2f} lv.')
