# Input
number_chrysanthemums = int(input())
number_roses = int(input())
number_tulips = int(input())
season = input()
holiday = input()
# Logic
arrange_bouquet = 2
total_flowers = number_tulips + number_roses + number_chrysanthemums
first_price = 0
total_price = 0
if season == 'Spring' or season == 'Summer':
    if number_tulips > 7 and season == 'Spring':
        if holiday == 'Y':
            first_price = 1.15 * (number_chrysanthemums * 2 + number_roses * 4.1 + number_tulips * 2.5) * 0.95\
                #Price raise holiday and discount for whole bouquet
        else:
            first_price = (number_chrysanthemums * 2 + number_roses * 4.1 + number_tulips * 2.5) * 0.95
    elif holiday == 'Y':
        first_price = (number_chrysanthemums * 2 + number_roses * 4.1 + number_tulips * 2.5) * 1.15
    else:
        first_price = (number_chrysanthemums * 2 + number_roses * 4.1 + number_tulips * 2.5)
elif season == 'Autumn' or season == 'Winter':
    if number_roses >= 10 and season == 'Winter':
        if holiday == 'Y':
            first_price = 1.15 * (number_chrysanthemums * 3.75 + number_roses * 4.5 + number_tulips * 4.15) * 0.9
                #Price raise holiday and discount for whole bouquet
        else:
            first_price = (number_chrysanthemums * 3.75 + number_roses * 4.5 + number_tulips * 4.15) * 0.9
    elif holiday == 'Y':
        first_price = (number_chrysanthemums * 3.75 + number_roses * 4.5 + number_tulips * 4.15) * 1.15
    else:
        first_price = (number_chrysanthemums * 3.75 + number_roses * 4.5 + number_tulips * 4.15)
if total_flowers > 20:
    total_price = first_price * 0.8 + 2
else:
    total_price = first_price + 2
# Output
print(f'{total_price:.2f}')