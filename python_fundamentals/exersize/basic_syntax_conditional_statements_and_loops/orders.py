number_of_orders = int(input())
current_order_price = 0
total_price = 0
for order in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    required_capsules = int(input())
    if not 0.01 <= price_per_capsule <= 100 or not 1 <= days <= 31 or \
            not 1 <= required_capsules <= 2000:
        continue
    current_order_price = price_per_capsule * days * required_capsules
    print(f'The price for the coffee is: ${current_order_price:.2f}')
    total_price += current_order_price
print(f'Total: ${total_price:.2f}')
