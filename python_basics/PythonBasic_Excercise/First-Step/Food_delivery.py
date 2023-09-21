chicken = 10.35
fish = 12.4
vegan = 8.15
delivery = 2.5
order_chicken = int(input())*chicken
order_fish = int(input())*fish
order_vegan = int(input())*vegan
total_order = order_chicken+order_fish+order_vegan
desert = total_order*0.2
total_sum = total_order+desert+delivery
print(round(total_sum,2))


