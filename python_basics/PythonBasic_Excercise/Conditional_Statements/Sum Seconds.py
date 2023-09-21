#User input
first_athlete = int(input())
second_athlete = int(input())
third_athlete = int(input())

#Logic
total_time = first_athlete + second_athlete + third_athlete
minutes = total_time // 60
seconds = total_time % 60
if seconds <= 9:
    print(f'{minutes}:{seconds:02d}')
else:
    print(f'{minutes}:{seconds}')

#Output