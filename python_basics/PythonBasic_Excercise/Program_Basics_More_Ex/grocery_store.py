price_vegetable_kilo = float(input())
price_fruit_kilo = float(input())
kilo_vegetable = int(input())
kilo_fruit = int(input())
total_vegetable = price_vegetable_kilo * kilo_vegetable
total_fruit = price_fruit_kilo * kilo_fruit
total_price = (total_vegetable + total_fruit)/1.94
print("%.2f" % total_price)
