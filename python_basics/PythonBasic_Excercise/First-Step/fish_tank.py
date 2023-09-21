length = int(input())
width = int(input())
height = int(input())
percentage = float(input())/100

volume_fish_tank = length*width*height
volume_in_litters = volume_fish_tank/1000
percentage_prefilled = volume_in_litters*percentage
total_volume_to_fill = volume_in_litters-percentage_prefilled
print(float(total_volume_to_fill))
