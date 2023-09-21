# Input
budget = float(input())
nights = int(input())
price_per_night = float(input())
percent_other = int(input())

# Logic
if nights > 7:
    price_per_night *= 0.95
total_spend = nights * price_per_night + percent_other / 100 * budget
left_money = abs(budget - total_spend)
if budget >= total_spend:
    print(f"Ivanovi will be left with {left_money:.2f} leva after vacation.")
else:
    print(f"{left_money:.2f} leva needed.")