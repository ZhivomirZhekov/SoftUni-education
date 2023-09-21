# Input
number_tournament = int(input())
starting_points = int(input())

total_points = 0
won_tournament = 0

# Logic
for i in range(number_tournament):
    stage_tournament = input()
    if stage_tournament == "W":
        won_tournament += 1
        total_points += 2000
    elif stage_tournament == 'F':
        total_points += 1200
    elif stage_tournament == 'SF':
        total_points += 720
average = total_points // number_tournament
total_points += starting_points
won_percent = won_tournament / number_tournament * 100
# Output
print(f'Final points: {total_points}')
print(f'Average points: {average}')
print(f'{won_percent:.2f}%')
