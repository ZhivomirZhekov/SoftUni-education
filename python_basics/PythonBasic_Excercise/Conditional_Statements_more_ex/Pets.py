# Input
from math import ceil, floor
days_absence = int(input())
food = int(input())
dog_food_per_day = float(input())
cat_food_per_day = float(input())
turtle_food_per_day = float(input())

# Logic
dog_food = days_absence * dog_food_per_day
cat_food = days_absence * cat_food_per_day
turtle_food = turtle_food_per_day * days_absence / 1000
total_eaten_food = dog_food + cat_food + turtle_food
difference = abs(total_eaten_food - food)

if total_eaten_food <= food:
    print(f'{floor(difference)} kilos of food left.') # Output
else:
    print(f'{ceil(difference)} more kilos of food are needed.') # Output