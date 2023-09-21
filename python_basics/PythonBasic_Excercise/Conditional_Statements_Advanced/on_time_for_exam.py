# Input
hour_exam = int(input())
minutes_exam = int(input())
hour_arrival = int(input())
minutes_arrival = int(input())
time_of_exam = hour_exam * 60 + minutes_exam
time_of_arrival = hour_arrival * 60 + minutes_arrival

# Logic
if time_of_arrival > time_of_exam:
    print('Late')
elif time_of_exam - 30 <= time_of_arrival <= time_of_exam:
    print('On time')
elif time_of_exam - 30 >= time_of_arrival:
    print('Early')

difference = abs(time_of_exam - time_of_arrival)
hour = difference // 60
minutes = difference % 60

if time_of_exam - 60 < time_of_arrival < time_of_exam:
    print(f'{minutes} minutes before the start')
elif time_of_arrival <= time_of_exam - 60:
    print(f'{hour}:{minutes:02d} hours before the start')
elif time_of_exam < time_of_arrival < time_of_exam + 60:
    print(f'{minutes} minutes after the start')
elif time_of_arrival >= time_of_exam + 60:
    print(f'{hour}:{minutes:02d} hours after the start')
# Ouput
