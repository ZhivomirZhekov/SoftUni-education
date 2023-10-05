fires_with_cells = input().split('#')
amount_of_water = int(input())
effort = 0
cells = []
total_fire = 0
for fire_type in fires_with_cells:
    fire_items = fire_type.split(' = ')
    type_of_fire = fire_items[0]
    value_of_cell = int(fire_items[1])
    if amount_of_water < value_of_cell:
        continue
    if type_of_fire == 'High' and 81 <= value_of_cell <= 125:
        effort += 0.25 * value_of_cell
        amount_of_water -= value_of_cell
    elif type_of_fire == 'Medium' and 51 <= value_of_cell <= 80:
        effort += 0.25 * value_of_cell
        amount_of_water -= value_of_cell
    elif type_of_fire == 'Low' and 1 <= value_of_cell <= 50:
        effort += 0.25 * value_of_cell
        amount_of_water -= value_of_cell
    else:
        continue
    cells.append(value_of_cell)
print('Cells:')
for cell in cells:
    print(f' - {cell}')
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {sum(cells)}')

