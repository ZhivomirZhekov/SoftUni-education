items_and_price = input().split('|')
budged = float(input())
bought_items_price = []
profit = 0
for equipment in items_and_price:
    item_with_price = equipment.split('->')
    item = item_with_price[0]
    price = float(item_with_price[1])
    if budged < price:
        continue
    if item == 'Clothes' and price > 50.00:
        continue
    elif item == 'Shoes' and price > 35.00:
        continue
    elif item == 'Accessories' and price > 20.50:
        continue
    else:
        budged -= price
        bought_items_price.append(price)
for cost in bought_items_price:
    budged += cost * 1.4    # sell the bought items with 40% margin
    profit += cost * 1.4 - cost
    print(f"{(cost * 1.4):.2f}", end=' ')
print("\n" f'Profit: {profit:.2f}')
if budged >= 150:
    print('Hello, France!')
else:
    print('Not enough money.')
