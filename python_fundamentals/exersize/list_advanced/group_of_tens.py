numbers = [int(s) for s in input().split(', ')]

current_group = 10

while numbers:
    numbers_in_current_group = [x for x in numbers if x <= current_group]
    print(f"Group of {current_group}'s: {numbers_in_current_group}")
    current_group += 10
    numbers = [number for number in numbers if number not in numbers_in_current_group]

