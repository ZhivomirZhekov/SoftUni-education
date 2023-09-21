# Input
desired_income = float(input())
# Logic
total_income = 0
while True:
    cocktail_name = input()
    if cocktail_name == 'Party!':
        difference = desired_income - total_income
        print(f"We need {difference:.2f} leva more.")
        print(f"Club income - {total_income:.2f} leva.")
        break
    number_cocktails = int(input())
    price_cocktail = len(cocktail_name)
    sum_price = number_cocktails * price_cocktail
    if sum_price % 2 != 0:
        total_income += 0.75 * price_cocktail * number_cocktails
    else:
        total_income += price_cocktail * number_cocktails
    if total_income >= desired_income:
        print("Target acquired.")
        print(f"Club income - {total_income:.2f} leva.")
        break
