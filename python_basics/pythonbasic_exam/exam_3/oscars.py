actor_name = input()
academy_points = float(input())
jury = int(input())
points = academy_points
is_true = False
for i in range(jury):
    name_jury = input()
    jury_points = float(input())
    points += len(name_jury) * jury_points / 2
    if points > 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {points:.1f}!")
        is_true = True
        break
if not is_true:
    points -= 1250.5
    print(f"Sorry, {actor_name} you need {abs(points):.1f} more!")