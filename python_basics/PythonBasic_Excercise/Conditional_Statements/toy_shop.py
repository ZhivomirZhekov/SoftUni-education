# Input
price_vacation = float(input())
number_puzzles = int(input())
number_speaking_dulls = int(input())
number_furry_bears = int(input())
number_minions = int(input())
number_trucks = int(input())

# Logic
puzzle_price = 2.6 * number_puzzles
speaking_dull_price = 3 * number_speaking_dulls
furry_bear_price = 4.1 * number_furry_bears
minion_price = 8.2 * number_minions
truck_price = 2 * number_trucks

sum_toys_order = number_puzzles + number_speaking_dulls + number_furry_bears + number_minions + number_trucks
total_price = puzzle_price + speaking_dull_price + furry_bear_price + minion_price + truck_price

if sum_toys_order >= 50:
    total_price *= 0.75

total_price *= 0.9

left_money = abs(total_price - price_vacation)

if total_price >= price_vacation:
    print(f'Yes! {left_money:.2f} lv left.')
else:
    print(f'Not enough money! {left_money:.2f} lv needed.')


# Output
