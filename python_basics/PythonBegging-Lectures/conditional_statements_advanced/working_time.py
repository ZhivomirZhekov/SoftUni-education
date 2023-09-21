# Input
hour = int(input())
day_of_week = input()

# Logic
if not day_of_week == 'Sunday' and 10 <= hour <= 18:
    print(f'open')
else:
    print(f'closed')
