quantity_food = float(input())
quantity_hay = float(input())
quantity_cover = float(input())
guinea_weight = float(input())
day_count = 0
while quantity_food >= 0 and quantity_hay >= 0 and quantity_cover >= 0:
    if day_count == 30:
        break
    day_count += 1
    quantity_food -= 0.3
    if day_count % 2 == 0:
        quantity_hay -= quantity_food * 0.05
    if day_count % 3 == 0:
        quantity_cover -= (1 / 3) * guinea_weight
if day_count == 30 :
    print(f"Everything is fine! Puppy is happy! Food: {quantity_food:.2f}, Hay: {quantity_hay:.2f},"
          f" Cover: {quantity_cover:.2f}.")
else:
    print("Merry must go to the pet store!")
