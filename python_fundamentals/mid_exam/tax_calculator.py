list_of_vehicles = input().split('>>')
family_tax = 0
heavy_duty_tax = 0
sports_tax = 0
total_tax = 0
for vehicle in list_of_vehicles:
    car_type , years , kilometers_traveled = vehicle.split()
    if car_type == "family":
        increase_tax_km_traveled = 12 * (int(kilometers_traveled) // 3000)
        decrease_tax = int(years) * 5
        family_tax = increase_tax_km_traveled + (50 - decrease_tax)
        print(f"A {car_type} car will pay {family_tax:.2f} euros in taxes.")
        total_tax += family_tax
    elif car_type == "heavyDuty":
        increase_tax_km_traveled = 14 * (int(kilometers_traveled) // 9000)
        decrease_tax = int(years) * 8
        heavy_duty_tax = increase_tax_km_traveled + (80 - decrease_tax)
        print(f"A {car_type} car will pay {heavy_duty_tax:.2f} euros in taxes.")
        total_tax += heavy_duty_tax
    elif car_type == "sports":
        increase_tax_km_traveled = 18 * (int(kilometers_traveled) // 2000)
        decrease_tax = int(years) * 9
        sports_tax = increase_tax_km_traveled + (100 - decrease_tax)
        print(f"A {car_type} car will pay {sports_tax:.2f} euros in taxes.")
        total_tax += sports_tax
    else:
        print("Invalid car type.")

print(f"The National Revenue Agency will collect {total_tax:.2f} euros in taxes.")