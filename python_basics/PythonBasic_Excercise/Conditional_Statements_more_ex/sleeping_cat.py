# Input
holidays = int(input())

# Logic
working_days = 365 - holidays
total_play_time = working_days*63 + holidays*127
sleeping_diff = abs(30000 - total_play_time)
diff_h = sleeping_diff // 60
diff_min = sleeping_diff % 60
if total_play_time > 30000:
    print(f'Tom will run away')
    print(f'{diff_h} hours and {diff_min} minutes more for play')
else:
    print(f'Tom sleeps well')
    print(f'{diff_h} hours and {diff_min} minutes less for play')

