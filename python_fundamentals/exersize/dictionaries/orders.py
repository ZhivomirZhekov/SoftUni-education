orders_dict = {}

while True:
    products = input()
    if products == "buy":
        break

    product , price , quantity = products.split()
    if product not in orders_dict.keys():
        orders_dict[product] = {}
        orders_dict[product]["quantity"] = 0
    orders_dict[product]["price"] = float(price)
    orders_dict[product]['quantity'] += float(quantity)

for key, value in orders_dict.items():
    total_price = value['price'] * value['quantity']
    print(f"{key} -> {total_price:.2f}")




