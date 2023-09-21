qty_excursion_sea = int(input())
qty_excursion_mountain = int(input())
total = 0
while True:
    if qty_excursion_sea == 0 and qty_excursion_mountain == 0:
        print(" Good job! Everything is sold.")
        break
    excursion = input()
    if excursion == 'Stop':
        break
    if qty_excursion_sea == 0 and qty_excursion_mountain == 0:
        print(" Good job! Everything is sold.")
        break
    if excursion == 'sea':
        if qty_excursion_sea <= 0:
            continue
        else:
            total += 680
            qty_excursion_sea -= 1
    elif excursion == 'mountain':
        if qty_excursion_mountain <= 0:
            continue
        else:
            total += 499
            qty_excursion_mountain -= 1
print(f"Profit: {total} leva.")