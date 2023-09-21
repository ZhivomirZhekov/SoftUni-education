# Input
name_club = input()
qty_matches = int(input())
wins = 0
equals = 0
loses = 0
points = 0
# Logic
for matches in range(qty_matches):
    result = input()
    if result == "W":
        wins += 1
        points += 3
    elif result == "D":
        equals += 1
        points += 1
    elif result == "L":
        loses += 1
if qty_matches > 0:
    percent_wins = wins / qty_matches * 100
    percent_equals = equals / qty_matches * 100
    percent_loses = loses / qty_matches * 100
    print(f"{name_club} has won {points} points during this season.")
    print(f"Total stats:")
    print(f"## W: {wins}")
    print(f"## D: {equals}")
    print(f"## L: {loses}")
    print(f"Win rate: {percent_wins:.2f}%")
elif qty_matches == 0:
    print(f"{name_club} hasn't played any games during this season.")