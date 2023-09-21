# Input
from math import ceil
people = int(input())
entrance_fee = float(input())
price_sunbed = float(input())
price_umbrella = float(input())

# Logic
total_entrance_tax = people * entrance_fee
total_umbrella = ceil(people / 2) * price_umbrella
total_sunbed = ceil(people * 0.75) * price_sunbed

total_sum = total_entrance_tax + total_sunbed + total_umbrella

print(f'{total_sum:.2f} lv.')

