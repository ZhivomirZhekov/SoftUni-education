# Input
velocity = float(input())
# Logic
if velocity <= 10:
    print(f'slow')
elif velocity <= 50:
    print(f'average')
elif velocity <= 150:
    print(f'fast')
elif velocity <= 1000:
    print(f'ultra fast')
else:
    print(f'extremely fast')