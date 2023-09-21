# Input
from math import floor , ceil
vineyard = int(input())
grape = float(input())
required_wine = int(input())
workers = int(input())

# Logic
harvest = vineyard * 0.4 # 40% from total vineyard for production of wine
produced_wine = harvest * grape / 2.5
difference = abs(produced_wine - required_wine)
left_wine_workers = difference / workers
if produced_wine < required_wine:
    print(f'It will be a tough winter! More {floor(difference)} liters wine needed.')
else:
    print(f'Good harvest this year! Total wine: {floor(produced_wine)} liters.')
    print(f'{ceil(difference)} liters left -> {ceil(left_wine_workers)} liters per person.')
