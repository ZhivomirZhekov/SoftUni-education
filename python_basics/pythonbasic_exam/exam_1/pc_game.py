# Input
qty_sold_games = int(input())
hearthstone = 0
fornite = 0
overwatch = 0
others = 0
# Logic
for games in range(qty_sold_games):
    game_name = input()
    if game_name == 'Hearthstone':
        hearthstone += 1
    elif game_name == 'Fornite':
        fornite += 1
    elif game_name == 'Overwatch':
        overwatch += 1
    else:
        others += 1
percent_hearthstone = hearthstone / qty_sold_games * 100
percent_fornite = fornite / qty_sold_games * 100
percent_overwatch = overwatch / qty_sold_games * 100
percent_others = others / qty_sold_games * 100
# Output
print(f"Hearthstone - {percent_hearthstone:.2f}%")
print(f"Fornite - {percent_fornite:.2f}%")
print(f"Overwatch - {percent_overwatch:.2f}%")
print(f"Others - {percent_others:.2f}%")
