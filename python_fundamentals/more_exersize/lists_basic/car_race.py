sequence_of_numbers = input().split()
list_of_numbers_as_int = []
left_racer_time = 0
right_racer_time = 0
for number in sequence_of_numbers:
    list_of_numbers_as_int.append(int(number))
half_of_list = len(list_of_numbers_as_int) // 2
left_racer = list_of_numbers_as_int[:half_of_list]
right_racer = list_of_numbers_as_int[half_of_list + 1::]

for time in left_racer:
    if time == 0:
        left_racer_time *= 0.8  # Reduce time with 20% if 0
    left_racer_time += time
for time in right_racer[::-1]:
    if time == 0:
        right_racer_time *= 0.8  # Reduce time with 20% if 0
    right_racer_time += time

if left_racer_time < right_racer_time:
    print(f"The winner is left with total time: {left_racer_time:.1f}")
else:
    print(f"The winner is right with total time: {right_racer_time:.1f}")
