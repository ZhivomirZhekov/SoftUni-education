from math import ceil
# Input
height_wall = int(input())
width_wall = int(input())
percent_not_paint = int(input()) / 100
total_to_paint = ceil(4 * height_wall * width_wall * (1 - percent_not_paint))
# Logic
while True:
    litters_paint = input()
    if litters_paint == "Tired!":
        print(f"{total_to_paint} quadratic m left.")
        break
    total_to_paint -= int(litters_paint)
    if total_to_paint < 0:
        print(f"All walls are painted and you have {abs(total_to_paint)} l paint left!")
        break
    elif total_to_paint == 0:
        print("All walls are painted! Great job, Pesho!")
        break
