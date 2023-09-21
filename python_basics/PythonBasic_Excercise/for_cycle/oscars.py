# Input
name_actor = input()
points_academy = float(input())
number_jury = int(input())
total_points = points_academy
# Logic
for i in range(number_jury):
    name_jury = input()
    point_jury = float(input())
    current_points = len(name_jury) / 2 * point_jury
    total_points += current_points
    if total_points > 1250.5:
        break
# Output
if total_points > 1250.5:
    print(f'Congratulations, {name_actor} got a nominee for leading role with {total_points:.1f}!')
else:
    diff = 1250.5 - total_points
    print(f'Sorry, {name_actor} you need {diff:.1f} more!')
