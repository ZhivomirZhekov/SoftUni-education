input_lines = int(input())
total_tank_capacity = 255
water_litters_counter = 0
for lines in range(input_lines):
    water_in_litters = int(input())
    if total_tank_capacity - water_in_litters < 0:
        print("Insufficient capacity!")
        continue
    total_tank_capacity -= water_in_litters
    water_litters_counter += water_in_litters
print(water_litters_counter)

