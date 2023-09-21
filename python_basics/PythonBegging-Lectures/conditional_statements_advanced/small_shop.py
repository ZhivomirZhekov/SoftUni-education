# Input
product = input()
city = input()
qty = float(input())
cost = 0

# Logic
coffee_sofia = 0.5
coffee_plovdiv = 0.4
coffee_varna = 0.45
water_sofia = 0.8
water_plovdiv = 0.7
water_varna = 0.7
beer_sofia = 1.2
beer_plovdiv = 1.15
beer_varna = 1.1
sweets_sofia = 1.45
sweets_plovdiv = 1.3
sweets_varna = 1.35
peanuts_sofia = 1.6
peanuts_plovdiv = 1.5
peanuts_varna = 1.55

if product == 'coffee':
    if city == 'Sofia':
        cost = qty * coffee_sofia
    elif city == 'Plovdiv':
        cost = qty * coffee_plovdiv
    elif city == 'Varna':
        cost = qty * coffee_varna
elif product == 'water':
    if city == 'Sofia':
        cost = qty * water_sofia
    elif city == 'Plovdiv':
        cost = qty * water_plovdiv
    elif city == 'Varna':
        cost = qty * water_varna
elif product == 'beer':
    if city == 'Sofia':
        cost = qty * beer_sofia
    elif city == 'Plovdiv':
        cost = qty * beer_plovdiv
    elif city == 'Varna':
        cost = qty * beer_varna
elif product == 'sweets':
    if city == 'Sofia':
        cost = qty * sweets_sofia
    elif city == 'Plovdiv':
        cost = qty * sweets_plovdiv
    elif city == 'Varna':
        cost = qty * sweets_varna
elif product == 'peanuts':
    if city == 'Sofia':
        cost = qty * peanuts_sofia
    elif city == 'Plovdiv':
        cost = qty * peanuts_plovdiv
    elif city == 'Varna':
        cost = qty * peanuts_varna

# Output
print(f'{cost}')
