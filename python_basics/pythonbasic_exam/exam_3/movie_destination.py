movie_budget = float(input())
destination = input()
season = input()
days = int(input())
cost = 0

if destination == 'Dubai':
    if season == 'Winter':
        cost = 45000 * days * 0.7
    elif season == 'Summer':
        cost = 40000 * days * 0.7
elif destination == 'Sofia':
    if season == 'Winter':
        cost = 17000 * days * 1.25
    elif season == 'Summer':
        cost = 12500 * days * 1.25
elif destination == 'London':
    if season == 'Winter':
        cost = 24000 * days
    elif season == 'Summer':
        cost = 20250 * days
total = movie_budget - cost

if total >= 0:
    print(f"The budget for the movie is enough! We have {total:.2f} leva left!")
else:
    print(f"The director needs {abs(total):.2f} leva more!")