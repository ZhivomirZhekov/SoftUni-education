budget = float(input())
serials = int(input())

for i in range(serials):
    serial_name = input()
    price = float(input())
    if serial_name == 'Thrones':
        price *= 0.5
        budget -= price
    elif serial_name == 'Lucifer':
        price *= 0.6
        budget -= price
    elif serial_name == 'Protector':
        price *= 0.7
        budget -= price
    elif serial_name == 'TotalDrama':
        price *= 0.8
        budget -= price
    elif serial_name == 'Area':
        price *= 0.9
        budget -= price
    else:
        budget -= price
if budget < 0:
    print(f"You need {abs(budget):.2f} lv. more to buy the series!")
else:
    print(f"You bought all the series and left with {budget:.2f} lv.")
