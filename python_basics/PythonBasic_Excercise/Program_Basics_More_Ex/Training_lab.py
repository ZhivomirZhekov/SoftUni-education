length_room_w = float(input())
width_room_h = float(input())
3 <= length_room_w <= width_room_h <= 100
width_with_corridor = width_room_h-1
work_place_w = 1.2
work_place_h = 0.7
length_seats = length_room_w/work_place_w
width_seats = width_with_corridor/work_place_h
total_seats = (int(length_seats)*int(width_seats))-3

print("%.f" % total_seats)

