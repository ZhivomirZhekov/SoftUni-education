# Input
from math import ceil, floor

magnolias = int(input())
hyacinths = int(input())
roses = int(input())
cactus = int(input())
present = float(input())

# Logic
price_magnolias = 3.25
price_hyacinths = 4
price_roses = 3.5
price_cactus = 8

total = price_magnolias * magnolias + price_hyacinths * hyacinths + price_roses * roses + price_cactus * cactus
tax = total * 0.05
total_finances = total - tax
difference = abs(total_finances - present)
if total_finances >= present:
    print(f'She is left with {floor(difference)} leva.')
else:
    print(f'She will have to borrow {ceil(difference)} leva.')