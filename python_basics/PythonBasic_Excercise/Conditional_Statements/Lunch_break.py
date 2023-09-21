# Input
from math import ceil
name_sitcom = input()
episode_time = int(input())
time_break = int(input())
# Logic
lunch_time = time_break * (1/8)
rest_time = time_break * (1/4)
total_time = episode_time + lunch_time + rest_time
time_left = ceil(abs(time_break - total_time))
if time_break >= total_time:
    print(f'You have enough time to watch {name_sitcom} and left with {time_left} minutes free time.')
else:
    print(f"You don't have enough time to watch {name_sitcom}, you need {time_left} more minutes.")
