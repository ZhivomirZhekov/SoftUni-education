# Input
fruit = input()
day_of_week = input()
qty = float(input())

result = 0
correct_input = True
# Logic
if fruit == 'banana':
    if day_of_week == 'Saturday' or day_of_week == 'Sunday':
        result = 2.7 * qty
    elif day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Wednesday' \
            or day_of_week == 'Thursday' or day_of_week == 'Friday':
        result = 2.5 * qty
    else:
        correct_input = False
elif fruit == 'apple':
    if day_of_week == 'Saturday' or day_of_week == 'Sunday':
        result = 1.25 * qty
    elif day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Wednesday' \
            or day_of_week == 'Thursday' or day_of_week == 'Friday':
        result = 1.2 * qty
    else:
        correct_input = False
elif fruit == 'orange':
    if day_of_week == 'Saturday' or day_of_week == 'Sunday':
        result = 0.90 * qty
    elif day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Wednesday' \
            or day_of_week == 'Thursday' or day_of_week == 'Friday':
        result = 0.85 * qty
    else:
        correct_input = False
elif fruit == 'grapefruit':
    if day_of_week == 'Saturday' or day_of_week == 'Sunday':
        result = 1.6 * qty
    elif day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Wednesday' \
            or day_of_week == 'Thursday' or day_of_week == 'Friday':
        result = 1.45 * qty
    else:
        correct_input = False
elif fruit == 'kiwi':
    if day_of_week == 'Saturday' or day_of_week == 'Sunday':
        result = 3 * qty
    elif day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Wednesday' \
            or day_of_week == 'Thursday' or day_of_week == 'Friday':
        result = 2.7 * qty
    else:
        correct_input = False
elif fruit == 'pineapple':
    if day_of_week == 'Saturday' or day_of_week == 'Sunday':
        result = 5.6 * qty
    elif day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Wednesday' \
            or day_of_week == 'Thursday' or day_of_week == 'Friday':
        result = 5.5 * qty
    else:
        correct_input = False
elif fruit == 'grapes':
    if day_of_week == 'Saturday' or day_of_week == 'Sunday':
        result = 4.2 * qty
    elif day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Wednesday' \
            or day_of_week == 'Thursday' or day_of_week == 'Friday':
        result = 3.85 * qty
    else:
        correct_input = False
else:
    correct_input = False
# Output
if correct_input:
    print(f'{result:.2f}')
else:
    print(f'error')
