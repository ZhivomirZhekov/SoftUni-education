# Input
type_flowers = input()
number_flowers = int(input())
budged = int(input())
price = 0
# Logic
rose = 5
dahlia = 3.8
tulip = 2.8
narcissus = 3
gladiolus = 2.5
if type_flowers == 'Roses':
    if number_flowers > 80:
        price = rose * number_flowers * 0.9 # Discount 10%
    else:
        price = rose * number_flowers
elif type_flowers == 'Dahlias':
    if number_flowers > 90:
        price = dahlia * number_flowers * 0.85 # Discount 15%
    else:
        price = dahlia * number_flowers

elif type_flowers == 'Tulips':
    if number_flowers > 80:
        price = tulip * number_flowers * 0.85  # Discount 10%
    else:
        price = tulip * number_flowers
elif type_flowers == 'Narcissus':
    if number_flowers < 120:
        price = narcissus * number_flowers * 1.15  # Discount 10%
    else:
        price = narcissus * number_flowers
elif type_flowers == 'Gladiolus': # Can be else
    if number_flowers < 80:
        price = gladiolus * number_flowers * 1.2 # Discount 10%
    else:
        price = gladiolus * number_flowers

differance = abs(price - budged)

if budged >= price:
    print(f'Hey, you have a great garden with {number_flowers} {type_flowers} and {differance:.2f} leva left.')
else:
    print(f'Not enough money, you need {differance:.2f} leva more.')
# Output
