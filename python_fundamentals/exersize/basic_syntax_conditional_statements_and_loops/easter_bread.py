budged = float(input())
price_flour_1kg = float(input())
price_pack_eggs = price_flour_1kg * 0.75  # price is 75% from 1kg flour
price_milk_250ml = price_flour_1kg * 1.25 / 4  # price of 1L milk is 25% more than price of flour 1kg
price_loaf = price_flour_1kg + price_pack_eggs + price_milk_250ml
loaf_count = 0
colored_eggs_count = 0
while budged > price_loaf:
    budged -= price_loaf
    colored_eggs_count += 3
    loaf_count += 1
    if loaf_count % 3 == 0:
        colored_eggs_count -= loaf_count - 2
print(f"You made {loaf_count} loaves of Easter bread! Now you have {colored_eggs_count} eggs and {budged:.2f}BGN left.")
