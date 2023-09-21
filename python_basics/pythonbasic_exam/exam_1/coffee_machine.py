# Logic

type_drink = input()
sugar = input()
qty_drinks = int(input())
# Logic
espresso = 0
cappuccino = 0
tea = 0
if type_drink == 'Espresso':
    if qty_drinks > 5:
        if sugar == 'Without':
            espresso = 0.9 * 0.65 * qty_drinks * 0.75
        elif sugar == 'Normal':
            espresso = 1 * qty_drinks * 0.75
        elif sugar == 'Extra':
            espresso = 1.2 * qty_drinks * 0.75
    else:
        if sugar == 'Without':
            espresso = 0.9 * 0.65 * qty_drinks
        elif sugar == 'Normal':
            espresso = 1 * qty_drinks
        elif sugar == 'Extra':
            espresso = 1.2 * qty_drinks
if type_drink == 'Cappuccino':
    if sugar == 'Without':
        cappuccino = 1 * 0.65 * qty_drinks
    elif sugar == 'Normal':
        cappuccino = 1.2 * qty_drinks
    elif sugar == 'Extra':
        cappuccino = 1.6 * qty_drinks
if type_drink == 'Tea':
    if sugar == 'Without':
        tea = 0.5 * 0.65 * qty_drinks
    elif sugar == 'Normal':
        tea = 0.6 * qty_drinks
    elif sugar == 'Extra':
        tea = 0.7 * qty_drinks
total = espresso + cappuccino + tea
if total > 15:
    total *= 0.8

# Output
print(f"You bought {qty_drinks} cups of {type_drink} for {total:.2f} lv.")
