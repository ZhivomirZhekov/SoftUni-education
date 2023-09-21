# Input
budged = int(input())
category = input()
number_people = int(input())
tickets = 0
needed_budged = 0
# Logic
vip = 499.99
normal = 249.99

if category == 'VIP':
    if 4 >= number_people >= 1:
        tickets = budged * 0.25 # 75% reserved for travel
        needed_budged = number_people * vip
    elif 9 >= number_people >= 5:
        tickets = budged * 0.4 # 60% reserved for travel
        needed_budged = number_people * vip
    elif 24 >= number_people >= 10:
        tickets = budged * 0.5 # 50% reserved for travel
        needed_budged = number_people * vip
    elif 49 >= number_people >= 25:
        tickets = budged * 0.6 # 40% reserved for travel
        needed_budged = number_people * vip
    elif number_people >= 50:
        tickets = budged * 0.75 # 25% reserved for travel
        needed_budged = number_people * vip
elif category == 'Normal':
    if 4 >= number_people >= 1:
        tickets = budged * 0.25 # 75% reserved for travel
        needed_budged = number_people * normal
    elif 9 >= number_people >= 5:
        tickets = budged * 0.4 # 60% reserved for travel
        needed_budged = number_people * normal
    elif 24 >= number_people >= 10:
        tickets = budged * 0.5 # 50% reserved for travel
        needed_budged = number_people * normal
    elif 49 >= number_people >= 25:
        tickets = budged * 0.6 # 40% reserved for travel
        needed_budged = number_people * normal
    elif number_people >= 50:
        tickets = budged * 0.75 # 25% reserved for travel
        needed_budged = number_people * normal
# Output
difference = abs(needed_budged - tickets)
if needed_budged <= tickets:
    print(f'Yes! You have {difference:.2f} leva left.')
else:
    print(f'Not enough money! You need {difference:.2f} leva.')

