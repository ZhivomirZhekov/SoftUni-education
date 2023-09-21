# Input
current_age = int(input())
laundry_price = float(input())
price_toy = int(input())

total_toys = 0
total_money = 0
current_birthday_money = 0
# Logic
for i in range(1,current_age + 1):
    if i % 2 == 0: # even birthday
        current_birthday_money += 10
        total_money += current_birthday_money - 1
    else: #odd birthday
        total_toys += 1
total_money += total_toys * price_toy
diff = abs(total_money - laundry_price)
# Output
if total_money >= laundry_price:
    print(f'Yes! {diff:.2f}')
else:
    print(f'No! {diff:.2f}')