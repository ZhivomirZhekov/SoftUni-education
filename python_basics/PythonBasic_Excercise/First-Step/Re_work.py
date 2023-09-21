cover = 1.5
paint = 14.5
paint_thinner = 5
bags = 0.4
total_cover = (int(input())+2)*cover
total_paint = (int(input())*1.1)*paint
total_thinner = int(input())*paint_thinner
total_hours = int(input())
total_sum = total_cover+total_paint+total_thinner+bags
work_hour_cost = total_sum*0.3
total_cost = total_sum+total_hours*work_hour_cost
print(total_cost)

