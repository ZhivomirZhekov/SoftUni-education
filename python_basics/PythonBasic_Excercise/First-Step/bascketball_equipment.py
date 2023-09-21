yearly_sub_training = int(input())
shoes = yearly_sub_training-(yearly_sub_training*0.4)
cloths = shoes-(shoes*0.2)
ball = cloths*(1/4)
accessories = ball*(1/5)
total_cost = yearly_sub_training+shoes+cloths+ball+accessories
print(total_cost)
