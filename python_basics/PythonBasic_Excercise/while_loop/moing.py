# Input
width = int(input())
length = int(input())
height = int(input())
volume = width * length * height
there_is_no_more_space = True

command = input()
while command != 'Done':
    number_boxes = int(command)
    volume -= number_boxes
    if volume < 0:
        there_is_no_more_space = False
        break
    command = input()
# Output
if there_is_no_more_space:
    print(f"{volume} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(volume)} Cubic meters more.")
