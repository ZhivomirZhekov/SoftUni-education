# Input
budget = float(input())
number_statists = int(input())
price_clothes = float(input())
# Logic
decor = budget * 0.10
if number_statists > 150:
    price_clothes *= 0.9
spend = decor + price_clothes * number_statists
difference = abs(budget - spend)
if budget >= spend:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
