x_height_house = float(input())
y_length_side_wall = float(input())
h_height_roof = float(input())
paint_green_consumption = 3.4
paint_red_consumption = 4.3
front_back_sides = (x_height_house * x_height_house - 1.2*2) + (x_height_house * x_height_house)
both_sides = 2 * x_height_house * y_length_side_wall - 2 * 1.5 * 1.5
roof = 2 * x_height_house * y_length_side_wall + 2 * (x_height_house * h_height_roof/2)
total_green_consumption = (front_back_sides + both_sides) / paint_green_consumption
total_red_consumption = roof / paint_red_consumption
print("%.2f" % total_green_consumption)
print("%.2f" % total_red_consumption)