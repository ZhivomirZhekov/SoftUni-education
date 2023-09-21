movie = input()
pack = input()
tickets = int(input())
bill = 0

if movie == 'John Wick':
    if pack == 'Drink':
        bill = 12 * tickets
    elif pack == 'Popcorn':
        bill = 15 * tickets
    elif pack == 'Menu':
        bill = 19 * tickets
elif movie == 'Star Wars':
    if tickets > 3:
        if pack == 'Drink':
            bill = 18 * tickets * 0.7
        elif pack == 'Popcorn':
            bill = 25 * tickets * 0.7
        elif pack == 'Menu':
            bill = 30 * tickets * 0.7
    else:
        if pack == 'Drink':
            bill = 18 * tickets
        elif pack == 'Popcorn':
            bill = 25 * tickets
        elif pack == 'Menu':
            bill = 30 * tickets
elif movie == 'Jumanji':
    if tickets == 2:
        if pack == 'Drink':
            bill = 9 * tickets * 0.85
        elif pack == 'Popcorn':
            bill = 11 * tickets * 0.85
        elif pack == 'Menu':
            bill = 14 * tickets * 0.85
    else:
        if pack == 'Drink':
            bill = 9 * tickets
        elif pack == 'Popcorn':
            bill = 11 * tickets
        elif pack == 'Menu':
            bill = 14 * tickets

print(f"Your bill is {bill:.2f} leva.")