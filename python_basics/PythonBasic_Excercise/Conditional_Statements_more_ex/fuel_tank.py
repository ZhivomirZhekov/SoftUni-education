# Input
fuel = input()
litters_in_tank = int(input())
nor
# Logic
if fuel == 'Diesel':
    if litters_in_tank >= 25:
        print(f'You have enough diesel.')
    else:
        print(f'Fill your tank with diesel!')
elif fuel == 'Gasoline':
    if litters_in_tank >=25:
        print(f'You have enough gasoline.')
    else:
        print(f'Fill your tank with gasoline!')
elif fuel == 'Gas':
    if litters_in_tank >= 25:
        print(f'You have enough gas.')
    else:
        print(f'Fill your tank with gas!')
else:
    print(f'Invalid fuel!')