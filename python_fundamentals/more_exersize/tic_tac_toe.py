lane_1_numbers = input().split()
lane_2_numbers = input().split()
lane_3_numbers = input().split()
player_1_win = False
player_2_win = False
for player in range(1 , 3):
    player = str(player)
    player_lane = [player , player , player]
    if lane_1_numbers == player_lane or lane_2_numbers == player_lane or lane_3_numbers == player_lane:
        if player == '1':
            player_1_win = True
        elif player == '2':
            player_2_win = True
        break
    for colum_index in range(3):
        if lane_1_numbers[colum_index] == player and lane_2_numbers[colum_index] == player \
                and lane_3_numbers[colum_index] == player:
            if player == '1':
                player_1_win = True
            elif player == '2':
                player_2_win = True
            break
    if lane_1_numbers[0] == player and lane_2_numbers[1] == player and lane_3_numbers[2] == player:
        if player == '1':
            player_1_win = True
        elif player == '2':
            player_2_win = True
        break
    elif lane_1_numbers[2] == player and lane_2_numbers[1] == player and lane_3_numbers[0] == player:
        if player == '1':
            player_1_win = True
        elif player == '2':
            player_2_win = True
        break
if player_1_win:
    print("First player won")
elif player_2_win:
    print("Second player won")
else:
    print("Draw!")